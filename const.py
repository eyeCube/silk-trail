'''


'''

K=1000

STATUS_HEALTHY      = 0
STATUS_ = 1

OZLB                = 12    # oz. in a pound
SADDLEBAG_LB        = 50    # max capacity per saddlebag (need camels)
CAMEL_CARRY         = 480   # max kg carry capacity per camel (need saddlebags)
CAMEL_CARRY_PENALTY = 30    # per unit of intensity of travel

SATIETY_MAX         = 72000
SATIETY_FOOD        = 1000  # satiety increase / oz. food
HUNGER_RATE         = 33    # satiety depletion / minute.

HYDRATION_MAX           = 300   # ounces
HYDRATION_WATER         = 1     # hydration increase / fluid oz.
DEHYDRATION_RATE        = 75    # base water consumption / day
EXERT_DEHYDRATION_RATE  = 5     # extra water consumption per unit of exertion

FOOD        = 1
WATER       = 2
TORCH       = 3
TINDER      = 4
CLOAK       = 5
SADDLEBAG   = 6
WEAPON      = 7
CAMEL       = 8   # eat grain  # required from Yumen onward
PENNY       = 101 # everywhere
SILVER      = 102 # everywhere
GOLD        = 103 # everywhere
GRAIN       = 201 # East China (feeds camels)
PAPER       = 301 # China
BRONZE      = 302 # China
PORCELAIN   = 303 # China
SILK        = 401 # West China
TEA         = 402 # West China
JADE        = 403 # West China
FABRIC      = 501 # India
SPICE       = 502 # India
DYE         = 503 # India
IVORY       = 504 # India
IDOL        = 505 # India
COTTON      = 601 # Central Asia
WOOL        = 602 # Central Asia
RICE        = 603 # Central Asia
SCROLL      = 701 # Middle East (culture / history / books)
FUR         = 801 # Europe
HONEY       = 802 # Europe
CATTLE      = 803 # Europe
HORSE       = 804 # Europe
MERCHANT    = 901 # need primary merchant to return to Zhengzhou.
                    # more merchants -> better chance of getting deals.
                    # start game with 5 merchants incl. one primary merchant;
                    # cannot gain new merchants throughout the game.
MERCENARY   = 902 # protect caravan using weapons
GUIDE       = 903 # required from Yumen onward

ITEMS={
    # weight - ounces
    # dura - durability 1-10 -- how easily it breaks
    # $EC - price in East China
    # $CC - price in Central China
    # $WC - price in West China
    # $In - price in India
    # $CA - price in Central Asia
    # $ME - price in Middle East
    # $Ty - price in Tyre, Lebanon
    # item      : name,             weight, dura,$EC, $CC, $WC, $In, $CA, $ME, $Ty
    FOOD        :("oz. of food",    1,      3,   4,   3,   3,   2,   3,   3,   4,),
    WATER       :("oz. of water",   1,      2,   1,   1,   1,   1,   2,   3,   3,),
    TORCH       :("torches",        10,     10,  3,   3,   4,   5,   6,   6,   8,),
    TINDER      :("bundles of tinder",0,    5,   1,   1,   1,   1,   1,   2,   3,),
    CLOAK       :("cloaks",         20,     6,   250, 175, 125, 150, 200, 250, 300,),
    CAMEL       :("camels",         0,      8,   2400,2000,1600,1200,800, 1000,1200,),
    SADDLEBAG   :("saddlebags",     0,      7,   50,  45,  40,  35,  30,  25,  50,),
    WEAPON      :("weapons",        OZLB*2, 9,   100, 150, 200, 250, 300, 350, 400,) ,
    COPPER      :("pennies",        0,      10,  1,   1,   1,   1,   1,   1,   1,),
    SILVER      :("silver coins",   0,      10,  10,  10,  10,  10,  10,  10,  10,),
    GOLD        :("gold coins",     0,      10,  100, 100, 100, 100, 100, 100, 100,),
    GRAIN       :("oz. of grain",   1,      4,   4,   6,   8,   10,  12,  14,  16,),
    PAPER       :("lb. of paper",   OZLB,   4,   480, 720, 800, 960, 1200,1440,1600,),
    BRONZE      :("bronzeware",     OZLB*1, 9,   80,  60,  75,  100, 125, 150, 200,),
    PORCELAIN   :("porcelainware",  8,      1,   20,  40,  80,  120, 180, 240, 360,),
    SILK        :("rolls of silk",  4,      4,   1600,1200,800, 1000,1600,2400,3600,),
    TEA         :("oz. of tea",     1,      3,   20,  40,  60,  80,  100, 150, 200,),
    JADE        :("oz. of jade",    1,      5,   500, 400, 300, 400, 500, 600, 750,),
    FABRIC      :("rolls of khadi", 4,      6,   2000,1500,1000,500, 1000,1250,1500,),
    SPICE       :("oz. of spices",  1,      5,   16,  12,  10,  6,   8,   10,  12,),
    DYE         :("oz. of dye",     1,      1,   100, 75,  40,  20,  60,  120, 160,),
    IVORY       :("lb. of ivory",   OZLB*1, 10,  1800,1600,1400,1200,1400,1600,2000,),
    IDOL        :("Buddha statues", 4,      5,   1600,1200,800, 400, 800, 1200,1600,),
    COTTON      :("rolls of cotton",4,      5,   800, 600, 400, 300, 200, 350, 500,),
    WOOL        :("rolls of wool",  4,      6,   700, 500, 350, 250, 150, 200, 300,),
    RICE        :("oz. of rice",    1,      4,   1,   2,   4,   6,   12,  18,  24,),
    SCROLL      :("scrolls",        6,      2,   32*K,28*K,24*K,20*K,16*K,12*K,8*K),
    FUR         :("rolls of fur",   4,      4,   600, 500, 400, 300, 200, 150, 100,),
    HONEY       :("oz. of honey",   1,      6,   75,  60,  50,  40,  30,  25,  20,),
    CATTLE      :("cattle",         0,      7,   1200,900, 600, 400, 450, 500, 400,),
    HORSE       :("horses",         0,      7,   1400,1000,800, 700, 650, 600, 500,),
}


# hunting:
# hunt for Jade in West China by rivers.


# weather
WEATHER_FAIR        = 0
WEATHER_COLD        = 1
WEATHER_FREEZING    = 2
WEATHER_HOT         = 3
WEATHER_BLAZING     = 4
WEATHER_STORM       = 5
WEATHER_DUSTSTORM   = 6
WEATHER = {
    # pace              :(name, hp/hour, thirst_rate)
    WEATHER_FAIR        :("fair",       1,      1,),
    WEATHER_COLD        :("cold",       -2,     1,),
    WEATHER_FREEZING    :("freezing",   -10,    1,),
    WEATHER_HOT         :("hot",        -6,     1.5,),
    WEATHER_BLAZING     :("blazing",    -10,    2,),
    WEATHER_STORM       :("storming",   -25,    1,),
    WEATHER_DUSTSTORM   :("dust storm", -50,    1,),
}

# paces
PACE_STOPPED        = 0
PACE_SLOW           = 1
PACE_MODERATE       = 2
PACE_BRISK          = 3
PACE_GRUELING       = 4
PACES = {
    # pace          :(name,        mi/day, %good, %bad events will happen
    PACE_STOPPED    :("stopped",   0,      0,      0,),
    PACE_SLOW       :("slow",      5,      8,      1,),
    PACE_MODERATE   :("moderate",  10,     5,      3,),
    PACE_BRISK      :("brisk",     15,     3,      5,),
    PACE_GRUELING   :("grueling",  20,     1,      8,),
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
TERRAIN_SANDY       = 0 # sandy desert
TERRAIN_ROCKY       = 1 # can be highland / mountainous
TERRAIN_BADLANDS    = 2 # highland / mountainous, ultra arid
TERRAIN_OASIS       = 3 # sandy desert punctuated with grassy oases
TERRAIN_GRASSY      = 4 # plains
TERRAIN_G_D         = 5 # partly grassy partly desert
TERRAINS={
    # terrain           :(name,         pace_mod, %good, %bad events will happen)
    TERRAIN_SANDY       :("sandy",      -1,       0,     0,),
    TERRAIN_ROCKY       :("rocky",      -2,       -1,    1,),
    TERRAIN_BADLANDS    :("badlands",   -3,       -2,    2,),
    TERRAIN_OASIS       :("oasis",      0,        10,    -3,),
    TERRAIN_GRASSY      :("grassy",     0,        2,     0,),
    TERRAIN_G_D         :("patchy",     0,        0,     0,),
}

CLIMATE_CONTINENTAL     = 1     # hot, humid summers w/ lots of rain, dry, cold winters
CLIMATE_TEMPERATE       = 2     # lots of rain, mild-cold weather
CLIMATE_HIGHLAND        = 3     # dry, cold weather
CLIMATE_MOUNTAINOUS     = 4     # arid, very cold winters
CLIMATE_COLDDESERT      = 5     # freezing snowy winters, mild sping/fall, dry/hot summer
CLIMATE_ARIDCONTINENTAL = 6     # long, dry, hot summer, irregular winter
CLIMATE_DESERT          = 7     # long, dry summers, short, cool winters, occasional violent storms in winter.
CLIMATES={
CLIMATE_CONTINENTAL     :("",),
}

PLACE_ROAD = 1
PLACE_VILLAGE = 2 # relatively tiny settlement
PLACE_TOWN = 3 # small city
PLACE_CITY = 4 # major city
PLACE_CAPITAL = 5 # most important city but may not be as large as other major cities
PLACES={
    PLACE_ROAD      :("road",),
    PLACE_VILLAGE   :("village",),
    PLACE_TOWN      :("town",),
    PLACE_CITY      :("city",),
    PLACE_CAPITAL   :("major city",),
}

REGION_EASTCHINA = 1
REGION_CENTRALCHINA = 2
REGION_WESTCHINA = 3
REGION_INDIA = 4
REGION_CENTRALASIA = 5
REGION_MIDDLEEAST = 6
REGION_TYRE = 7
REGIONS = {
    REGION_EASTCHINA    : "East China", 
    REGION_CENTRALCHINA : "Central China", 
    REGION_WESTCHINA    : "West China", 
    REGION_INDIA        : "India", 
    REGION_CENTRALASIA  : "Central Asia", 
    REGION_MIDDLEEAST   : "Middle East", 
    REGION_TYRE         : "Mediterranean",
}

GOVT_YUAN        = 1
GOVT_CHAGATAI    = 2
GOVT_ILKHANATE   = 3
GOVERNMENTS={
    GOVT_YUAN       : "Yuan Dynasty",
    GOVT_CHAGATAI   : "Chagatai Khanate", # has Mongolian raiders until 02/01/1326
    GOVT_ILKHANATE  : "Ilkhanate",
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
            "n2":(OZLB,OZLB*2,OZLB*3,OZLB*4,OZLB*5,),
            "i2":(FOOD, WATER, BULLET,),
        },
    },
]

MONTHS = { # Julian calendar
    1 : ('name':"Ianuarius", 'temp':12,),
    2 : ('name':"Februarius", 'temp':12,),
    3 : ('name':"Martius", 'temp':12,),
    4 : ('name':"Aprilis", 'temp':12,),
    5 : ('name':"Iunius", 'temp':12,),
    6 : ('name':"Maius", 'temp':12,),
    7 : ('name':"Quintilis", 'temp':12,),
    8 : ('name':"Sextilis", 'temp':12,),
    9 : ('name':"September", 'temp':12,),
    10: ('name':"October", 'temp':12,),
    11: ('name':"November", 'temp':12,),
    12: ('name':"December",   'temp':12,),  
}
YEARS = {
    1 : "Rat",
    2 : "Ox",
    3 : "Tiger",
    4 : "Rabbit",
    5 : "Dragon",
    6 : "Snake",
    7 : "Horse",
    8 : "Goat",
    9 : "Monkey",
    10: "Rooster",
    11: "Dog",
    12: "Pig",
}
HISTORY = {
    "stop mongol raids" : (2*12 + 2, "Khan Ozbeg reopens friendly relations with the Yuan Dynasty.",),
    "civil war begins" : (5*12 + 11, "El Temur overthrows the court of Shangdu, resulting in the Yuan Dynasty erupting into civil war.",),
}




