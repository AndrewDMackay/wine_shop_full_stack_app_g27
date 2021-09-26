
class Producer:
    def __init__(self, producer_name, country, region, producer_description, id = None):
        self.producer_name = producer_name
        self.country = country
        self.region = region
        self.producer_description = producer_description
        self.id = id


# class Producer: properties, and priorities..

# Priority	        Property	            Example Input
# 1	                Producer Name	        Radikon
# 1	                Country	                Italy
# 1	                Region	                Friuli
# 1	                Producer Description	? [ See below ]
# 2	                Total Stock By Producer	?

# Producer Description Example..

# * Radikon is a 12 hectare estate on the Slovenian border of Italy, a truly unique winery. 
# Stanko Radikon captained this groundbreaking winery since 1995, paving the way for the natural wine movement. 
# He realised that the local indigenous grape, Ribolla Gialla, needed to be treated differently to other varieties. 
# So, he turned to his grandfather’s method of vinification, which involved seven days of skin maceration. 
# Stanko experimented with this technique and today's wines have around three months of maceration, along with long periods of barrel and bottle ageing. 
# Working this way has meant that he has been able to cut out the use of sulphites entirely. 
# The specially designed bottles allow for better development in bottle, and he only uses the highest quality corks that avoid cork taint. 
# His grape selection is so meticulous, it is usual for a whole vine to go into making just one single bottle. 
# His wines are truly fascinating, with unbelievable complexity, high ageing potential and profound, wild, flavours.  
# Since Stanko passed away recently, his son Saša Radikon continues in his father's tradition, maintaining the same high standards.