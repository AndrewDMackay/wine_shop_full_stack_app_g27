
import pdb

from models.wine import Wine
from models.producer import Producer

import repositories.wine_repository as wine_repository
import repositories.producer_repository as producer_repository


wine_repository.delete_all()
producer_repository.delete_all()

producer1 = Producer("Producer 1", "Country 1", "Region 1", "Producer Description 1")
producer_repository.save(producer1)

producer2 = Producer("Producer 2", "Country 2", "Region 2", "Producer Description 2")
producer_repository.save(producer2)

producer3 = Producer("Producer 3", "Country 3", "Region 3", "Producer Description 3")
producer_repository.save(producer3)

producer_repository.select_all()


wine1 = Wine("Wine Name 1", producer1, 6, 5.00, 10.00)
wine_repository.save(wine1)

wine2 = Wine("Wine Name 2", producer1, 6, 5.00, 10.00)
wine_repository.save(wine2)

wine3 = Wine("Wine Name 3", producer1, 6, 5.00, 10.00)
wine_repository.save(wine3)

wine4 = Wine("Wine Name 4", producer2, 6, 5.00, 10.00)
wine_repository.save(wine4)

wine5 = Wine("Wine Name 5", producer2, 6, 5.00, 10.00)
wine_repository.save(wine5)

wine6 = Wine("Wine Name 6", producer2, 6, 5.00, 10.00)
wine_repository.save(wine6)

wine7 = Wine("Wine Name 7", producer3, 6, 5.00, 10.00)
wine_repository.save(wine7)

wine8 = Wine("Wine Name 8", producer3, 6, 5.00, 10.00)
wine_repository.save(wine8)

wine9 = Wine("Wine Name 9", producer3, 6, 5.00, 10.00)
wine_repository.save(wine9)

wine_repository.select_all()




pdb.set_trace()

