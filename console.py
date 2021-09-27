
import pdb

from models.wine import Wine
from models.producer import Producer

import repositories.wine_repository as wine_repository
import repositories.producer_repository as producer_repository


wine_repository.delete_all()
producer_repository.delete_all()

producer1 = Producer("Radikon", "Italy", "Friuli", "Saša Radikon.")
producer_repository.save(producer1)

producer2 = Producer("Pheasant's Tears", "Georgia", "Kakheti", "Gela Patalashvili")
producer_repository.save(producer2)

producer3 = Producer("Sepp Muster", "Austria", "Susteiermark", "Sepp, and Maria Muster")
producer_repository.save(producer3)

producer_repository.select_all()


wine1 = Wine("Vino Bianco IGT, Slatnick", producer1, 24, 15.00, 30.00)
wine_repository.save(wine1)

wine2 = Wine("Oslavje", producer1, 12, 18.00, 36.00)
wine_repository.save(wine2)

wine3 = Wine("Jakot", producer1, 4, 19.00, 38.00)
wine_repository.save(wine3)

wine4 = Wine("Kisi", producer2, 18, 9.00, 18.00)
wine_repository.save(wine4)

wine5 = Wine("Rkatsiteli", producer2, 12, 10.00, 20.00)
wine_repository.save(wine5)

wine6 = Wine("Mtsvane", producer2, 4, 12.00, 24.00)
wine_repository.save(wine6)

wine7 = Wine("Sauvignon, Vom Opok", producer3, 24, 12.00, 24.00)
wine_repository.save(wine7)

wine8 = Wine("Gräfin", producer3, 12, 14.00, 28.00)
wine_repository.save(wine8)

wine9 = Wine("Erde", producer3, 0, 18.00, 36.00)
wine_repository.save(wine9)

wine_repository.select_all()




pdb.set_trace()

