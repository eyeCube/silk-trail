
from const import *

class Place:
    def __init__(self,
        name:str,
        kind:int, region:int, terrain:int, climate:int,
        length=0
        ):
        '''
            name: place's name as it was in medieval times
            kind: PLACE_ const
            region: REGION_ const
            terrain: TERRAIN_ const
            climate: CLIMATE_ const
            length: how many miles wide? Applies only to Road types
        '''
        self.kind = kind
        self.name = name
        self.region = region
        self.terrain = terrain
        self.climate = climate
        self.length = length

class CaravanTrail:
    def __init__(self):
        
        # create settlements
        
        zhengzhou = Place(
            "Zhengzhou",
            PLACE_CITY, REGION_EASTCHINA, TERRAIN_OASIS, CLIMATE_CONTINENTAL,
            length = 0
            )
        xian = Place(
            "Xi'an",
            PLACE_CAPITAL, REGION_CENTRALCHINA, TERRAIN_OASIS, CLIMATE_CONTINENTAL,
            length = 0
            )
        baoji = Place(
            "Baoji",
            PLACE_CITY, REGION_CENTRALCHINA, TERRAIN_OASIS, CLIMATE_CONTINENTAL,
            length = 0
            )
        tianshui = Place(
            "Tianshui",
            PLACE_CITY, REGION_CENTRALCHINA, TERRAIN_OASIS, CLIMATE_CONTINENTAL,
            length = 0
            )
        lanzhou = Place(
            "Lanzhou",
            PLACE_CITY, REGION_CENTRALCHINA, TERRAIN_OASIS, CLIMATE_CONTINENTAL,
            length = 0
            )
        liangzhou = Place(
            "Liangzhou",
            PLACE_CITY, REGION_CENTRALCHINA, TERRAIN_OASIS, CLIMATE_CONTINENTAL,
            length = 0
            )
        suzhou = Place(
            "Suzhou",
            PLACE_TOWN, REGION_CENTRALCHINA, TERRAIN_OASIS, CLIMATE_CONTINENTAL,
            length = 0
            )
        yumen = Place(
            "Yumen",
            PLACE_TOWN, REGION_CENTRALCHINA, TERRAIN_OASIS, CLIMATE_CONTINENTAL,
            length = 0
            )
        anxi = Place(
            "Anxi",
            PLACE_VILLAGE, REGION_CENTRALCHINA, TERRAIN_OASIS, CLIMATE_CONTINENTAL,
            length = 0
            )
        dunhuang = Place(
            "Dunhuang",
            PLACE_TOWN, REGION_CENTRALCHINA, TERRAIN_OASIS, CLIMATE_CONTINENTAL,
            length = 0
            )
        
        self.path_1 = [zhengzhou, xian, baoji, tianshui, lanzhou, liangzhou,
                       suzhou, yumen, anxi, dunhuang]
        self.path_2a = [hami, turpan, urumqi, dzungaria]
        self.path_2b = [qarkilik, niya, keriya, khotan, yarkant, kashgar]
        self.path_3 = [torugart, andijan, kokand, tashkent, samarkand, merv,
                  mashhad, ray, mahadan, kermanshah, baquba, baghdad,
                  fallujah, duraeuropos, palmyra, damascus, tyre]

        # create roads
        roads_1 = {hash("Zhengzhou") + hash("Xi'an") : zhengzhou_xian}
    
        










