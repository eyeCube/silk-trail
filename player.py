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
        self._hpMax = hp
        self._satiety = SATIETY_MAX
        self._status = STATUS_HEALTHY

    def __str__(self):
        return "Character: '{}'".format(self._name)
        
    @property
    def name(self): return self._name
    @property
    def status(self): return self._status
    @property
    def hp(self): return self._hp
    @property
    def hpMax(self): return self._hpMax
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
        self._hp = min(self._hpMax, self._hp + value)

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

    def manageHydration(self, waterAmount, exertion):
        waterUsage = DEHYDRATION_RATE + exertion*EXERT_DEHYDRATION_RATE
        if waterUsage > waterAmount:
            self.hp -= 10
            # (chance to) lose health and/or get sick
            # message: drink from muddy water source / dehydrate
        return waterUsage

# end class

class Player:
    def __init__(self, month=1, year=2, startloc="Xi'an"):
        # after init, call initialize function(s)
        self.characters = {}
        self.toKill = set()
        self.day = 1
        self.month = month
        self.year = year    # 1 == 1324, 12 == 1335 (max)
        self.items = {}
        self.weather = WEATHER_FAIR
        self.pace = PACE_STOPPED
        self.location = startloc    # (string) current Place we are at
        self.position = 0 # (float) miles: position inside the current location
    # end def
        
    def initializeCharacters(self):
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

    def getItemName(self, itemID):
        return ITEMS[itemID][0]
    def getItemWeight(self, itemID):
        return ITEMS[itemID][1]
    def getItemDurability(self, itemID):
        return ITEMS[itemID][2]
    def getItemCost(self, itemID, location=None):
        if not location:
            location = self.location
        regionID = self.trail.getPlaceByName(location).region
        return ITEMS[itemID][2 + regionID]
    def getItemQuantity(self, itemID):
        return self.items.get(itemID, 0)
    def setItemQuantity(self, itemID, quantity):
        self.items[itemID] = quantity
    def changeItemQuantity(self, itemID, quantity):
        self.items[itemID] = max(0, self.getItemQuantity(itemID) + quantity)
    def calcValue(self, itemID, barterRate=1.0):
        return barterRate * self.getItemQuantity(itemID) * self.getItemCost(itemID)

    def getIntensity(self):
        return INTENSITY[self.weather].get(self.pace, 0)
    def getCarryCapacity(self):
        # simple rules. Camels are picky.
        #   Each camel can carry either one character OR up to X kg supplies
        v = CAMEL_CARRY - self.getIntensity()*CAMEL_CARRY_PENALTY
        camelMax = v * (self.getItemQuantity(CAMEL) - len(self.characters))
        return max(0, min(camelMax, self.saddlebags*SADDLEBAG_KG))
##    def getCarryWeight(self):
##        return ceil(
##            (self.food + self.water + self.guns*GUNS_WEIGHT)/OZLB
##            )
##    def getDefense(self):
##        return min(len(self.characters), self.guns)

    def kill(self, name): # call to mark character as dead
        self.toKill.add(name)
    def processDead(self): # call at end of cycle
        for name in self.toKill:
            del self.characters[name]
        self.toKill = set()

    def feed(self, name, x=1):
        if self.food < x:
            msg.give("You don't have {} oz. of food; you only have {}.".format(x, self.food))
            return
        
        self.food -= x
        self.characters[name].feed(x)
    # end def

    def passDay(self, thirstRate=1):
        ''' thirst_rate is float, based on climate '''
        
        def _advanceMonth():
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1
                
        intensity = self.getIntensity()
        self.day += 1
        
        if (self.month == 2 and self.day == 28
            or self.month % 2 == 0 and self.day == 30
            or self.day == 31):
            _advanceMonth()
            
        for character in self.characters.values():
            thirstExertion = round(thirstRate*intensity)
            
            if self.water > 0:
                self.water = character.manageHydration(
                    self.water,
                    exertionLevel = thirst_exertion
                    )
                if self.water <= 0:
                    self.water = 0
                    msg.out("You've run out of water!")
                
            if self.food > 0:
                self.food = character.manageSatiety(
                    self.food,
                    exertionLevel = intensity
                    )
                if self.food <= 0:
                    self.food = 0
                    msg.out("You've run out of food!")

        # feed and give water to all mercenaries, guides, camels, cattle, horses.
    # end def
            
    def getDate(self):
        string = ""
        string += MONTHS[self.month]['name'] + " "
        string += self.day + ", "
        string += "Year of the " + ZODIAC[self.year]

##    def get_time(self):
##        string = ""
##        string += "{}:".format(str(self.time//(60*24) + 1))
##        string += "{}".format((self.time//60) % 24).rjust(2, '0') + ":"
##        string += "{}".format(self.time % 60).rjust(2, '0')
##        return string

    def setTime(self, value):
        self.time = max(0, value)
        
    def runGame(self):
        if self.game_state == GAMESTATE_TRAVEL:
            self.runTravel()

    def runTravel(self):
        elapsed = 0
        t = 120
        while t > 0:
            t -= 5
            elapsed += 5
            for ev
        
        self.pass_minutes(elapsed)
        
        






        
