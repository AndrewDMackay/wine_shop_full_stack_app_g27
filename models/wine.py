
from flask.scaffold import F


class Wine:
    def __init__(self, wine_name, producer, stock, net_price, sell_price, id = None):
        self.wine_name = wine_name
        self.producer = producer
        self.stock = stock
        self.net_price = net_price
        self.sell_price = sell_price
        self.id = id


    # Pseudo-Code for PDA.. 

    # Function to check stock levels, versus a threshold, and display feedback..

    # Function, 'check stock'..

    # If stock is below the set threshold..
    # Print or return 'Stock Low..'

    # If stock is equal to none..
    # Print or return 'Out Of Stock..

    # If stock is anything else..
    # Print or return 'Stock Normal'..

    # Add icons in html alongside text feedback..


    def check_stock(wine):
        if wine.stock <=5:
            return "Stock Low.."
        elif wine.stock == 0:
            return "Out Of Stock.."
        else:
            return "Stock Level Normal"


    def calculate_margin(self):
        inc_vat_price = self.net_price * 1.2
        percentage_margin = ((self.sell_price - inc_vat_price) / self.sell_price) * 100
        return round(percentage_margin, 2)
      

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

