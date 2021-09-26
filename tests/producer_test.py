
import unittest

from models.producer import Producer
from models.wine import Wine

class TestProducer(unittest.TestCase):
    
    def setUp(self):
        self.producer1 = Producer("producer1", "country1", "region1", "producer_description1")
        self.wine1 = Wine("wine1", self.producer1, 6, 5.00, 10.00)
        
    
    def test_producer_has_producer_name(self):
        self.assertEqual("producer1", self.producer.producer_name)
        
        
    def test_producer_has_producer(self):
        self.assertEqual("producer1", self.producer.producer)
       
        
    def test_producer_has_stock(self):
        self.assertEqual(6, self.producer.stock)

    def test_producer_has_net_price(self):
        self.assertEqual(5.00, self.producer.net_price)

    def test_producer_has_sell_price(self):
        self.assertEqual(10.00, self.producer.sell_price)


    

