'''

'''

from math import ceil
import random

from const import *
import ui
import trail

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
        self._plague = 0

    def __str__(self):
        return self._name #"Character: '{}'".format(self._name)
        
    @property
    def hp(self): # use harm / heal functions to alter hp stat
        return self._hp
    @property
    def hp_max(self):
        return self._hp_max
    @property
    def name(self):
        return self._name
    
##    @property
##    def hydration(self): return self._hydration
    @property
    def satiety(self): # use feed / metabolize functions to alter satiety stat
        return self._satiety

    def set_plague(self):
        self._plague = max(self._plague, 1)
    @property
    def plague(self):
        return self._plague

    # --- status update --- #
    def update(self):
        
        # plague
        if self._plague > 0:
            
            # end of disease -- either get better, or die
            if self._plague >= 7 + int(random.random()*14):
                if random.random()*100 <= 66: # 66% of people die of plague w/o antibiotics
                    self.die("plague")
                else:
                    self._plague = 0
                    ui.show("{} recovers from plague.".format(self.name))
                    ui.draw('event_character_recover')

            # progress disease
            self._plague += 1
            if self._plague == 4:
                ui.show("{} becomes ill from plague.".format(self.name))
                ui.draw('event_character_ill')
            elif self._plague == 7:
                ui.show("{}'s plague symptoms are at their peak.".format(self.name))
                ui.draw('event_character_critical')
        # end if
        
        # 
    # end def

    def status(self):
        score = 0
        # 0 == healthy
        # 1 == unhealthy
        # 2 == ill
        # 3 == critical
        
        if self._plague >= 7:
            score = max(score, 3)
        elif self._plague >= 4:
            score = max(score, 2)
        elif self._plague >= 1:
            score = max(score, 1)
            
        if self.satiety <= SATIETY_MAX * 0.05:
            score = max(score, 3)
        elif self.satiety <= SATIETY_MAX * 0.2:
            score = max(score, 2)
        elif self.satiety <= SATIETY_MAX * 0.5:
            score = max(score, 1)
            
        if self.hp <= self.hp_max * 0.25:
            score = max(score, 3)
        elif self.hp <= self.hp_max * 0.5:
            score = max(score, 2)
        elif self.hp <= self.hp_max * 0.75:
            score = max(score, 1)

        return score
        

    @_checkdead
    def die(self, cause):
        self.dead = True
        self._player.kill(self.name)
        ui.draw('event_character_death', self, cause)
    
    @_checkdead
    def harm(self, value):
        self._hp -= value
        if self._hp <= 0:
            self.die('exhaustion')
    @_checkdead
    def heal(self, value):
        self._hp = min(self._hp_max, self._hp + value)

    @_checkdead
    def metabolize(self, x=1, exertion_level=1):
        self._satiety -= x*HUNGER_RATE*exertion_level
        if self._satiety <= 0:
            self.die('hunger')
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
            # - (chance to) lose health and/or get sick
            # - message: drink from muddy water source / dehydrate
        return waterUsage

# end class

class Player:
    def __init__(self, month=1, year=2, startloc=trail.Trail.zhengzhou):
        # - after init, call initialize_ function(s)
        self.characters = {}
        self.tokill = set()
        self.day = 1
        self.month = month
        self.year = year       # 1 == 1324
        self.inventory = {}
        self.weather = WEATHER_FAIR
        self.pace = PACE_STOPPED
        self.location = startloc

        self.events = self.populate_events()
        
    # end def
        
    def initialize_characters(self):
        self.characters = {}
        i = 1
        while i <= 5:
            name = ui.get("Name for party member #{}?".format(i))
            if (not name or name in self.characters):
                ui.show(">> Try again; invalid entry.")
                continue
            i += 1
            char = Character(self, name)
            self.characters.update({name : char})

        for character in self.characters.values():
            ui.show(character)
    # end def

    def get_intensity(self):
        return INTENSITY[self.weather].get(self.pace, 0)
    def get_carry_capacity(self):
        # - simple rules. Camels are picky.
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
            ui.show("You don't have {} oz. of food; you only have {}.".format(x, self.food))
            return
        
        self.food -= x
        self.characters[name].feed(x)
    # end def

    def add_status(self, character, status):
        character.status = max(character.status, status)

    def pass_day(self, thirst_rate=1):
        ''' thirst_rate is float, basedmiles on climate '''
        
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
                    ui.show("You've run out of water!")
                
            if self.food > 0:
                self.food = character.manage_satiety(
                    self.food,
                    exertion_level = intensity
                    )
                if self.food <= 0:
                    self.food = 0
                    ui.show("You've run out of food!")

        # - feed and give water to all mercenaries, guides, camels, cattle, horses.
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
        mode = 'wait'
        
        while True:
            if mode == 'wait':
                self.get_input_mode(mode)

            elif mode == 'travel':
                elapsed = 0
                if self.miles > 0:
                    miles_traveled = min(self.miles, PACES[self.pace][1])
                    self.miles -= miles_traveled
                    elapsed += miles_traveled
                    
                    self.perform_events()

                    thirst_rate = 1 #temp
                    self.pass_day(thirst_rate)

                    self.mode = 'wait' # temporary until full GUI is complete

            elif mode == 'inventory':
                pass
            
            elif mode == '':
                pass

    def populate_events(self):
        # - create the event list for use by perform_events
        # - we select randomly from this list, so higher quantity == more common occurrence
        events = []
        events += ['thief'] * 10
        events += ['find'] * 10
        events += ['sick'] * 10
        plague_chance = PLACES[self.location.kind][1]
        for char in self.characters:
            plague_change += char.plague
        events += ['plague'] * plague_chance
        return events
            
    def perform_events(self):
        # - possibly perform random events
        if random.random()*100 < 10:
            event = random.choice(self.events)

            # - thief: lose supplies OR defend yourself
            if event == 'thief':
                ui.show('You encounter a thief.')
                ui.draw('event_thief')
                ui.show_menu({'f':'fight', 't':'talk', 'r':'run', 's':'submit',})
                inp=ui.get()
                if inp=='f':
                    pass
                elif inp=='t':
                    pass
                elif inp=='r':
                    pass
                elif inp=='s':
                    pass

            # - find: gain supplies OR get ambushed (rare) OR leave them behind
            elif event == 'find':
                ui.show('You find an abandoned cart with some supplies.')
                ui.draw('event_find')
                ui.show_menu({'t':'take', 'l':'leave',})
                inp=ui.get()
                if inp=='t':
                    pass
                elif inp=='l':
                    pass

            # - sick: contract moderate illness
            elif event == 'sick':
                chars = self.characters.values()
                healthy_chars = []
                for char in chars:
                    if char.status < STATUS_PLAGUE:
                        healthy_chars.append(char)
                if len(healthy_chars) == 0:
                    return
                character = random.choice(healthy_chars)
                ui.show('{} contracts dysentery.'.format(character))
                ui.draw('event_character_contract')
                self.add_status(character, STATUS_PLAGUE)

            # - plague: contract major illness
            elif event == 'plague':
                chars = self.characters.values()
                healthy_chars = []
                for char in chars:
                    if char.status < STATUS_PLAGUE:
                        healthy_chars.append(char)
                if len(healthy_chars) == 0:
                    return
                character = random.choice(healthy_chars)
                ui.show('{} has contracted plague.'.format(character))
                ui.draw('event_character_contract')
                self.add_status(character, STATUS_PLAGUE)

    def get_input_mode(self, mode):
        self.show_menu()
        inp = ui.get()
        if inp == 't':
            return 'travel'
        if inp == 'i':
            return 'inventory'

    def show_menu(self):
        ui.show_menu({'t':'travel', 'i':'inventory'})






        
