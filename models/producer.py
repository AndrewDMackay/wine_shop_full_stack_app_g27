
from flask.scaffold import F

class Producer:
    def __init__(self, producer_name, country, region, winemaker, id = None):
        self.producer_name = producer_name
        self.country = country
        self.region = region
        self.winemaker = winemaker
        self.id = id

        

