from selBs4 import *

class returnpricesuseinput:

    def __init__(self, bc):
        self.bc = bc 
    def returnAmazonPrice(self):
        soup2 = selBs4('https://www.amazon.com/s?k=' + self.bc).returnsoup()
        floatPrice = -1
        for item in soup2.find("span", {"class": "a-offscreen"}):
            priceTag= str(item)
            if "$" in priceTag:
                indexSign = priceTag.find("$")
                floatPrice = float(priceTag[indexSign+1:].replace("</span>","")) 
                print("the price is $" + str(floatPrice))
                return floatPrice
            else:
                print("?")

    def returnWalmartPrice(self):
        soup2 = selBs4('https://www.walmart.com/search/?query=' + self.bc).returnsoup()
        floatPrice = -1
        for item in soup2.find_all("span", {"class": "visuallyhidden"}):
            priceTag= str(item)
            if "$" in priceTag:
                indexSign = priceTag.find("$")
                floatPrice = float(priceTag[indexSign+1:].replace("</span>","")) 
                print("the price is $" + str(floatPrice))
                return floatPrice
            else:
                print("?")

    def returneBayPrice(self):
        soup2 = selBs4('https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + self.bc + "&_sop=15").returnsoup()
        floatPrice = -1
        for item in soup2.find_all("span", {"class": "s-item__price"}):
            priceTag= str(item)
            if "$" in priceTag:
                indexSign = priceTag.find("$")
                floatPrice = float(priceTag[indexSign+1:].replace("</span>","")) 
                print("the price is $" + str(floatPrice))
                return floatPrice
            else:
                print("?")       
            
            
