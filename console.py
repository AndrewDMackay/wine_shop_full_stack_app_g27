
import pdb

from models.wine import Wine
from models.producer import Producer

import repositories.wine_repository as wine_repository
import repositories.producer_repository as producer_repository


wine_repository.delete_all()
producer_repository.delete_all()

producer1 = Producer("Radikon", "Italy", "Friuli", "Radikon is a 12 hectare estate on the Slovenian border of Italy, a truly unique winery.")
producer_repository.save(producer1)

producer2 = Producer("Producer 2", "Country 2", "Region 2", "Producer Description 2")
producer_repository.save(producer2)

producer3 = Producer("Producer 3", "Country 3", "Region 3", "Producer Description 3")
producer_repository.save(producer3)

producer_repository.select_all()

# class Producer: properties, and priorities..

# Priority	        Property	            Example Input
# 1	                Producer Name	        Radikon
# 1	                Country	                Italy
# 1	                Region	                Friuli
# 1	                Winemaker	            Saša Radikon

# class Wine: properties, and priorities..

# Priority	Property	            Example Input
# 1	        Name	                Vino Bianco IGT, Slatnick 
# 1	        Producer Name           Radikon [ Import from Producer Class.. ]
# 1	        Stock                   ?  [ Unit, Bottles ]
# 1	        Buying Cost	            ?.??  [ Ex or Inc Vat ]
# 1	        Selling Cost	        ?.??  [ Inc Vat ]
# 1	        Country                 Italy  [ Import from Producer Class.. ]
# 2	        Region                  Friuli [ Import from Producer Class.. ]
# 2	        Vintage	                2019
# 2	        Colour	                Orange
# 2	        Dominant Grape	        80% Chardonnay, 20% Tocai
# 2	        ABV	                    14%
# 3	        Type	                Still, Skin Contact
# 3	        Bottle Size	            75cl
# 3	        Wine Style	            Full-bodied


wine1 = Wine("Vino Bianco IGT, Slatnick", producer1, 12, 16.00, 32.00)
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

