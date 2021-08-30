
from const import *

class Place:
    def __init__(self,
        name:str,
        kind:int, region:int, terrain:int, climate:int, govt:int,
        length=0,
        _west1=None, _west2=None, _east1=None, _east2=None
        ):
        '''
            name: place's name as it was in medieval times
            kind: PLACE_ const
            region: REGION_ const
            terrain: TERRAIN_ const
            climate: CLIMATE_ const
            length: how many miles wide? Applies only to Road types
            _west / _east 1 & 2: what Place is west / east of here?
                there may be two options in one direction in cases of forked paths
        '''
        self.kind = kind
        self.name = name
        self.region = region
        self.terrain = terrain
        self.climate = climate
        self.govt = govt
        self.length = length

class Trail: # Caravan Trail 
    def __init__(self):
        
        # create settlements
        
        zhengzhou = Place(
            "Zhengzhou",
            PLACE_CAPITAL, REGION_EASTCHINA, TERRAIN_OASIS,
            CLIMATE_TEMPERATE, GOVT_YUAN,
            length = 0,
            _west1 = "Zhengzhou-Xi'an", _east1 = None
            )
        zhengzhou_xian = Place(
            "Zhengzhou-Xi'an",
            PLACE_ROAD, REGION_EASTCHINA, TERRAIN_G_D,
            CLIMATE_CONTINENTAL, GOVT_YUAN,
            length = 300,
            _west1 = "Xi'an", _east1 = "Zhengzhou"
            )
        xian = Place(
            "Xi'an",
            PLACE_CAPITAL, REGION_CENTRALCHINA, TERRAIN_OASIS,
            CLIMATE_CONTINENTAL, GOVT_YUAN,
            length = 0,
            _west1 = "Xi'an-Baoji", _east1 = "Zhengzhou-Xi'an"
            )
        xian_baoji = Place(
            "Xi'an-Baoji",
            PLACE_ROAD, REGION_EASTCHINA, TERRAIN_G_D,
            CLIMATE_CONTINENTAL, GOVT_YUAN,
            length = 110,
            _west1 = "Baoji", _east1 = "Xi'an"
            )
        baoji = Place(
            "Baoji",
            PLACE_CITY, REGION_CENTRALCHINA, TERRAIN_OASIS,
            CLIMATE_CONTINENTAL, GOVT_YUAN,
            length = 0,
            _west1 = "Baoji-Tianshui", _east1 = "Xi'an-Baoji"
            )
        baoji_tianshui = Place(
            "Baoji-Tianshui",
            PLACE_ROAD, REGION_EASTCHINA, TERRAIN_G_D,
            CLIMATE_CONTINENTAL, GOVT_YUAN,
            length = 110,
            _west1 = "Tianshui", _east1 = "Baoji"
            )
        tianshui = Place(
            "Tianshui",
            PLACE_CITY, REGION_CENTRALCHINA, TERRAIN_OASIS,
            CLIMATE_CONTINENTAL, GOVT_YUAN,
            length = 0,
            _west1 = "Tianshui-Lanzhou", _east1 = "Baoji-Tianshui"
            )
        tianshui_lanzhou = Place(
            "Tianshui-Lanzhou",
            PLACE_ROAD, REGION_EASTCHINA, TERRAIN_G_D,
            CLIMATE_CONTINENTAL, GOVT_YUAN,
            length = 190,
            _west1 = "Lanzhou", _east1 = "Tianshui"
            )
        lanzhou = Place(
            "Lanzhou",
            PLACE_CITY, REGION_CENTRALCHINA, TERRAIN_OASIS,
            CLIMATE_CONTINENTAL, GOVT_YUAN,
            length = 0,
            _west1 = "Lanzhou-Liangzhou", _east1 = "Tianshui-Lanzhou"
            )
        lanzhou_liangzhou = Place(
            "Lanzhou-Liangzhou",
            PLACE_ROAD, REGION_EASTCHINA, TERRAIN_SANDY,
            CLIMATE_CONTINENTAL, GOVT_YUAN,
            length = 170,
            _west1 = "Liangzhou", _east1 = "Lanzhou"
            )
        liangzhou = Place(
            "Liangzhou",
            PLACE_CITY, REGION_CENTRALCHINA, TERRAIN_OASIS,
            CLIMATE_CONTINENTAL, GOVT_YUAN,
            length = 0,
            _west1 = "Liangzhou-Suzhou", _east1 = "Lanzhou-Liangzhou"
            )
        liangzhou_suzhou = Place(
            "Liangzhou-Suzhou",
            PLACE_ROAD, REGION_EASTCHINA, TERRAIN_SANDY,
            CLIMATE_CONTINENTAL, GOVT_YUAN,
            length = 275,
            _west1 = "Suzhou", _east1 = "Liangzhou"
            )
        suzhou = Place(
            "Suzhou",
            PLACE_TOWN, REGION_CENTRALCHINA, TERRAIN_OASIS,
            CLIMATE_CONTINENTAL, GOVT_YUAN,
            length = 0,
            _west1 = "Suzhou-Yumen", _east1 = "Liangzhou-Suzhou"
            )
        suzhou_yumen = Place(
            "Suzhou-Yumen",
            PLACE_ROAD, REGION_EASTCHINA, TERRAIN_SANDY,
            CLIMATE_CONTINENTAL, GOVT_YUAN,
            length = 95,
            _west1 = "Yumen", _east1 = "Suzhou"
            )
        yumen = Place(
            "Yumen",
            PLACE_TOWN, REGION_CENTRALCHINA, TERRAIN_OASIS,
            CLIMATE_CONTINENTAL, GOVT_YUAN,
            length = 0,
            _west1 = "Yumen-Anxi", _east1 = "Liangzhou-Yumen"
            )
        yumen_anxi = Place(
            "Yumen-Anxi",
            PLACE_ROAD, REGION_EASTCHINA, TERRAIN_SANDY,
            CLIMATE_CONTINENTAL, GOVT_YUAN,
            length = 85,
            _west1 = "Anxi", _east1 = "Yumen"
            )
        anxi = Place(
            "Anxi",
            PLACE_VILLAGE, REGION_CENTRALCHINA, TERRAIN_OASIS,
            CLIMATE_CONTINENTAL, GOVT_YUAN,
            length = 0,
            _west1 = "Anxi-Dunhuang", _east1 = "Yumen-Anxi"
            )
        anxi_dunhuang = Place(
            "Anxi-Dunhuang",
            PLACE_ROAD, REGION_EASTCHINA, TERRAIN_SANDY,
            CLIMATE_CONTINENTAL, GOVT_YUAN,
            length = 75,
            _west1 = "Dunhuang", _east1 = "Anxi"
            )
        dunhuang = Place(
            "Dunhuang",
            PLACE_TOWN, REGION_CENTRALCHINA, TERRAIN_OASIS,
            CLIMATE_CONTINENTAL, GOVT_YUAN,
            length = 0,
            _west1 = "Dunhuang-Hami", _west2 = "Dunhuang-Qarkilik",
            _east1 = "Anxi-Dunhuang"
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
    
        










