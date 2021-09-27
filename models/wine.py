
from flask.scaffold import F


class Wine:
    def __init__(self, wine_name, producer, stock, net_price, sell_price, id = None):
        self.wine_name = wine_name
        self.producer = producer
        self.stock = stock
        self.net_price = net_price
        self.sell_price = sell_price
        self.id = id


    def check_stock(wine):
        if wine.stock <=5:
            return "Stock Low.."
        elif wine.stock == 0:
            return "Out Of Stock.."
        else:
            return "Stock Level Normal"


    def calculate_margin(wine):
        inc_vat_price = wine.net_price * 1.2
        percentage_margin = (wine.sell_price - inc_vat_price) / wine.sell_price
        return (f"{percentage_margin}%")
      

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

