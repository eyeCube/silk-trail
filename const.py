'''


'''

STATUS_HEALTHY      = 0
STATUS_ = 1

CAMEL       = 0
SADDLEBAG   = 1
GUN         = 2
BULLET      = 3
FOOD        = 4
WATER       = 5
TORCH       = 6
TINDER      = 7
CLOAK       = 8

ITEMS={
    # item      : name,         weight, price,  price_rise
    CAMEL       :("camel",      0,      800,    10,),
    SADDLEBAG   :("saddlebag",  0,      50,     10,),
    GUN         :("gun",        OZKG*4, 400,    100,),
    BULLET      :("bullet",     0,      1,      10,),
    FOOD        :("food",       1,      10,     100,),
    WATER       :("water",      1,      1,      100,),
    TORCH       :("torch",      8,      50,     10,),
    TINDER      :("tinder",     0,      5,      10,),
    CLOAK       :("cloak",      20,     20,     10,),
}

OZKG                = 36    # oz. in a KG
SADDLEBAG_KG        = 50    # max capacity per saddlebag (need camels)
CAMEL_CARRY         = 450   # max kg carry capacity per camel (need saddlebags)
CAMEL_CARRY_PENALTY = 30    # per unit of intensity of travel

SATIETY_MAX         = 72000
SATIETY_FOOD        = 1000  # satiety increase / oz. food
HUNGER_RATE         = 33    # satiety depletion / minute.

HYDRATION_MAX       = 1440
HYDRATION_WATER     = 60    # hydration increase / fluid oz.
DEHYDRATION_RATE    = 1     # hydration depletion / minute (* intensity)

# weather
WEATHER_FAIR        = 0
WEATHER_COLD        = 1
WEATHER_HOT         = 2
WEATHER_BLAZING     = 3
WEATHER_DUSTSTORM   = 4
WEATHER_FREEZING    = 5
WEATHER = {
    # pace              :(name, hp/hour, thirst_rate)
    WEATHER_FAIR        :("fair",       0,      1,),
    WEATHER_COLD        :("cold",       -2,     1,),
    WEATHER_HOT         :("hot",        6,      1.5,),
    WEATHER_BLAZING     :("blazing",    -10,    2,),
    WEATHER_DUSTSTORM   :("dust storm", -25,    1,),
    WEATHER_FREEZING    :("blizzard",   -25,    1,),
}

# paces
PACE_STOPPED        = 0
PACE_SLOW           = 1
PACE_MODERATE       = 2
PACE_BRISK          = 3
PACE_GRUELING       = 4
PACES = {
    # pace          :(name,        km/day, %good, %bad events will happen
    PACE_STOPPED    :("stopped",   0,      0,      0,),
    PACE_SLOW       :("slow",      4,      8,      1,),
    PACE_MODERATE   :("moderate",  6,      5,      3,),
    PACE_BRISK      :("brisk",     8,      3,      5,),
    PACE_GRUELING   :("grueling",  10,     1,      8,),
}

# meals / eating
MEALS_PER_DAY       = 3

MEALPLAN_FAST       = 0
MEALPLAN_RATION     = 1
MEALPLAN_DIET       = 2
MEALPLAN_HEALTHY    = 3
MEALPLAN_GLUTTONY   = 4
MEALPANS={
    # meal plan         :(name, oz./person/meal, hp/meal
    MEALPLAN_FAST       :("fasting",    0, -5,),
    MEALPLAN_RATION     :("ration",     0, -5,),
    MEALPLAN_DIET       :("diet",       0, -5,),
    MEALPLAN_HEALTHY    :("healthy",    0, -5,),
    MEALPLAN_GLUTTONY   :("gluttony",   0, -5,),
}

# terrain
TERRAIN_SANDY = 0
TERRAIN_ROCKY = 1
TERRAIN_BADLANDS = 2
TERRAIN_OASIS = 3
TERRAINS={
    # terrain           :(name,         pace_mod, %good, %bad events will happen)
    TERRAIN_SANDY       :("sandy",      0,        0,     0,),
    TERRAIN_ROCKY       :("rocky",      -1,       -1,    1,),
    TERRAIN_BADLANDS    :("badlands",   -2,       -2,    2,),
    TERRAIN_OASIS       :("oasis",      0,        10,    -3,),
}

# intensity table
INTENSITY = {
    WEATHER_FAIR : {
        PACE_SLOW       : 1,
        PACE_MODERATE   : 2,
        PACE_BRISK      : 3,
        PACE_GRUELING   : 4,
    },
    WEATHER_COLD : {
        PACE_SLOW       : 2,
        PACE_MODERATE   : 3,
        PACE_BRISK      : 4,
        PACE_GRUELING   : 5,
    },
    WEATHER_HOT : {
        PACE_SLOW       : 2,
        PACE_MODERATE   : 4,
        PACE_BRISK      : 6,
        PACE_GRUELING   : 8,
    },
    WEATHER_BLAZING : {
        PACE_SLOW       : 3,
        PACE_MODERATE   : 6,
        PACE_BRISK      : 9,
        PACE_GRUELING   : 12,
    },
}

# events
EVENTS=[ # idea: instead of doing this, just make a big function that handles
    # everything relating to events. Each event is so different that it doesn't
    # make much sense to have a table for event data.
    # Then again, there could be event "types" which have predetermined
    # functionality such that adding a new event of that type would be easy.
    # Most events fall into a few categories:
    #   - lose-items
    #   - gain-items
    #   - change-status : change status of a character (sickness / health)
    #   - move : change location of party relative to current location (int)
    #   - move-abs : change location of party to absolute location (int)
    {
        "name":"thief",
        "type":"lose-items",
        "text":"thief steals {n1} {i1} and {n2} {i2}.",
        "data":{
            "n1":(1,1,2,2,3,),
            "i1":(CAMEL, SADDLEBAG, GUN, CLOAK, TORCH,),
            "n2":(OZKG,OZKG*2,OZKG*3,OZKG*4,OZKG*5,),
            "i2":(FOOD, WATER, BULLET,),
        },
    },
]







