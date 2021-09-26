
import pdb

from models.wine import Wine
from models.producer import Producer

import repositories.wine_repository as wine_repository
import repositories.producer_repository as producer_repository


wine_repository.delete_all()
producer_repository.delete_all()

producer1 = Producer("producer_name1", "country1", "region1", "producer_description1")
producer_repository.save(producer1)

producer2 = Producer("producer_name2", "country2", "region2", "producer_description2")
producer_repository.save(producer2)

producer3 = Producer("producer_name3", "country3", "region3", "producer_description3")
producer_repository.save(producer3)

producer_repository.select_all()


wine1 = Wine("wine_name1", producer1, 6, 5.00, 10.00)
wine_repository.save(wine1)

wine2 = Wine("wine_name2", producer1, 6, 5.00, 10.00)
wine_repository.save(wine2)

wine3 = Wine("wine_name3", producer1, 6, 5.00, 10.00)
wine_repository.save(wine3)

wine4 = Wine("wine_name4", producer1, 6, 5.00, 10.00)
wine_repository.save(wine4)

wine5 = Wine("wine_name5", producer1, 6, 5.00, 10.00)
wine_repository.save(wine5)

wine6 = Wine("wine_name6", producer1, 6, 5.00, 10.00)
wine_repository.save(wine6)

wine7 = Wine("wine_name7", producer1, 6, 5.00, 10.00)
wine_repository.save(wine7)

wine8 = Wine("wine_name8", producer1, 6, 5.00, 10.00)
wine_repository.save(wine8)

wine9 = Wine("wine_name9", producer1, 6, 5.00, 10.00)
wine_repository.save(wine9)

wine_repository.select_all()




pdb.set_trace()

