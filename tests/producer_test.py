
import unittest

from models.producer import Producer
from models.wine import Wine


class TestProducer(unittest.TestCase):
    
    def setUp(self):
        self.producer = Producer("producer1", "country1", "region1", "winemaker1", True)
        self.wine = Wine("wine1", self.producer, 6, 5.00, 10.00)
        
    
    def test_producer_has_producer_name(self):
        self.assertEqual("producer1", self.producer.producer_name)
        
        
    def test_producer_has_country(self):
        self.assertEqual("country1", self.producer.country)
       
        
    def test_producer_has_region(self):
        self.assertEqual("region1", self.producer.region)


    def test_producer_has_winemaker(self):
        self.assertEqual("winemaker1", self.producer.winemaker)

    def test_producer_has_winemaker(self):
        self.assertEqual(True, self.producer.active)


