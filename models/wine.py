
class Wine:
    def __init__(self, wine_name, producer, stock, net_price, sell_price, id = None):
        self.wine_name = wine_name
        self.producer = producer
        self.stock = stock
        self.net_price = net_price
        self.sell_price = sell_price
        self.id = id


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
# 3	        Type	                Still, Skin Contact
# 2	        Dominant Grape	        80% Chardonnay, 20% Tocai
# 2	        ABV	                    14%
# 3	        Wine Description	    ? [ See below.. ]
# 3	        Bottle Size	            75cl
# 3	        Wine Style	            Full-bodied

# Product Description Example..

# Slatnik Radikon, 80% Chardonnay, 20% Tocai, 12 days on the skins, biodynamic, a complex yet easy drinking orange wine. 
# It is fantastic wine, rich and bold but as with all of Radikon's wines, there is this vein of acid which makes it so fresh.