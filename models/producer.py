
from flask.scaffold import F

class Producer:
    def __init__(self, producer_name, country, region, winemaker, id = None):
        self.producer_name = producer_name
        self.country = country
        self.region = region
        self.winemaker = winemaker
        self.id = id


# class Producer: properties, and priorities..

# Priority	        Property	            Example Input
# 1	                Producer Name	        Radikon
# 1	                Country	                Italy
# 1	                Region	                Friuli
# 1	                Winemaker	            Saša Radikon


