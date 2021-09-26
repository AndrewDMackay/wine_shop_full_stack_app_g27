
import unittest

from models.wine import Wine
from models.producer import Producer


class TestWine(unittest.TestCase):
    
    def setUp(self):
        self.producer = Producer("producer1", "country1", "region1", "producer_description1")
        self.wine = Wine("wine1", "producer1", 6, 5.00, 10.00)
        
    
    def test_wine_has_wine_name(self):
        self.assertEqual("wine1", self.wine.wine_name)
        
        
    def test_wine_has_producer(self):
        self.assertEqual("producer1", self.wine.producer)
       
        
    def test_wine_has_stock(self):
        self.assertEqual(6, self.wine.stock)


    def test_wine_has_net_price(self):
        self.assertEqual(5.00, self.wine.net_price)


    def test_wine_has_sell_price(self):
        self.assertEqual(10.00, self.wine.sell_price)


    