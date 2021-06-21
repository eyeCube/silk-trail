'''

'''

from math import ceil

from const import *
import msg
import dice

class Character:
    
    def _checkdead(func):
        def wrapper(self):
            if not self.dead:
                func(self)
        return wrapper
    
    def __init__(self, player, name:str, hp=100):
        self.dead = False
        self._player = player
        self._name = name
        self._hp = hp       # health, includes tiredness / sleepiness / hydration
        self._hp_max = hp
        self._satiety = SATIETY_MAX
        self._status = STATUS_HEALTHY

    def __str__(self):
        return "Character: '{}'".format(self._name)
        
    @property
    def hp(self): return self._hp
    @property
    def name(self): return self._name
    @property
    def hp_max(self): return self._hp_max
    @property
    def status(self): return self._status
##    @property
##    def hydration(self): return self._hydration
    @property
    def satiety(self): return self._satiety

    @_checkdead
    def die(self):
        self.dead = True
        self._player.kill(self.name)
        msg.give("{} died.".format(self.name))
    
    @_checkdead
    def harm(self, value):
        self._hp -= value
        if self._hp <= 0:
            self.die()
    @_checkdead
    def heal(self, value):
        self._hp = min(self._hp_max, self._hp + value)

    @_checkdead
    def metabolize(self, x=1, exertion_level=1):
        self._satiety -= x*HUNGER_RATE*exertion_level
        if self._satiety <= 0:
            self.die()
    @_checkdead
    def feed(self, x=1):
        self._satiety = min(SATIETY_MAX, self._satiety + x*SATIETY_FOOD)
        
##    @_checkdead
##    def dehydrate(self, x=1, exertion_level=1):
##        self._hydration -= x*DEHYDRATION_RATE*(0.5 + 0.5*exertion_level)
##        if self._hydration <= 0:
##            self.die()
##    @_checkdead
##    def hydrate(self, x=1):
##        self._hydration = min(HYDRATION_MAX, self._hydration + x*HYDRATION_WATER)

    def manage_hydration(self, waterAmount, exertion):
        waterUsage = DEHYDRATION_RATE + exertion*EXERT_DEHYDRATION_RATE
        if waterUsage > waterAmount:
            self.hp -= 10
            # (chance to) lose health and/or get sick
            # message: drink from muddy water source / dehydrate
        return waterUsage

# end class

class Player:
    def __init__(self, month=1, startloc="Xi'an"):
        # after init, call initialize_ function(s)
        self.characters = {}
        self.tokill = set()
        self.day = 1
        self.month = month
        self.year = 2       # 1325 - year of the Ox
        self.food = 0       # oz.
        self.money = 0      # $
        self.water = 0      # fluid oz.
        self.guns = 0       # 
        self.bullets = 0    #
        self.saddlebags = 0 # bags carry X kg each. Require camels to use.
        self.camels = 0     # required to traverse desert. Carry saddlebags.
        self.torches = 0    # required to travel by night or in dark places.
        self.tinder = 0     # one use per tinder; required to start a fire.
        self.weather = WEATHER_FAIR
        self.pace = PACE_STOPPED
        self.location = startloc
    # end def
        
    def initialize_characters(self):
        self.characters = {}
        i = 1
        while i <= 5:
            name = msg.get("Name for party member #{}: ".format(i))
            if (not name or name in self.characters):
                msg.give(">> Try again; invalid entry.")
                continue
            i += 1
            char = Character(self, name)
            self.characters.update({name : char})

        for character in self.characters.values():
            msg.give(character)
    # end def

    def get_intensity(self):
        return INTENSITY[self.weather].get(self.pace, 0)
    def get_carry_capacity(self):
        # simple rules. Camels are picky.
        #   Each camel can carry either one character OR up to X kg supplies
        v = CAMEL_CARRY - self.get_intensity()*CAMEL_CARRY_PENALTY
        camelMax = v * (self.camels - len(self.characters))
        return max(0, min(camelMax, self.saddlebags*SADDLEBAG_KG))
    def get_carry_weight(self):
        return ceil(
            (self.food + self.water + self.guns*GUNS_WEIGHT)/OZLB
            )
    def get_defense(self):
        return min(len(self.characters), self.guns)

    def kill(self, name): # call to mark character as dead
        self.tokill.add(name)
    def process_dead(self): # call at end of cycle
        for name in self.tokill:
            del self.characters[name]
        self.tokill = set()

    def feed(self, name, x=1):
        if self.food < x:
            msg.give("You don't have {} oz. of food; you only have {}.".format(x, self.food))
            return
        
        self.food -= x
        self.characters[name].feed(x)
    # end def

    def pass_day(self, thirst_rate=1):
        ''' thirst_rate is float, based on climate '''
        
        def _advance_month():
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1
                
        intensity = self.get_intensity()

        self.day += 1
        
        if (self.month == 2 and self.day == 28
            or self.month % 2 == 0 and self.day == 30
            or self.day == 31):
            _advance_month()
            
        for character in self.characters.values():
            thirst_exertion = round(thirst_rate*intensity)
            
            if self.water > 0:
                self.water = character.manage_hydration(
                    self.water,
                    exertion_level = thirst_exertion
                    )
                if self.water <= 0:
                    self.water = 0
                    msg.out("You've run out of water!")
                
            if self.food > 0:
                self.food = character.manage_satiety(
                    self.food,
                    exertion_level = intensity
                    )
                if self.food <= 0:
                    self.food = 0
                    msg.out("You've run out of food!")

        # feed and give water to all mercenaries, guides, camels, cattle, horses.
    # end def
            
    def get_date(self):
        string = ""
        string += MONTHS[self.month]['name'] + " "
        string += self.day + ", "
        string += "Year of the " + YEARS[self.year]

##    def get_time(self):
##        string = ""
##        string += "{}:".format(str(self.time//(60*24) + 1))
##        string += "{}".format((self.time//60) % 24).rjust(2, '0') + ":"
##        string += "{}".format(self.time % 60).rjust(2, '0')
##        return string

    def set_time(self, value):
        self.time = max(0, value)
        
    def run_game(self):
        if self.game_state == GAMESTATE_TRAVEL:
            self.run_travel()

    def run_travel(self):
        elapsed = 0
        t = 120
        while t > 0:
            t -= 5
            elapsed += 5
            for ev
        
        self.pass_minutes(elapsed)
        
        






        
