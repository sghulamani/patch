from selBs4 import *

class walmartPrice:
    soup2 = selBs4('https://www.walmart.com/search/?query=' + "060549008080" ).returnsoup()
    floatprice = -1
    for item in soup2.find_all("span", {"class": "visuallyhidden"}):
        priceTag= str(item)
        if "$" in priceTag:
            indexSign = priceTag.find("$")
            floatPrice = float(priceTag[indexSign+1:].replace("</span>","")) 
        else:
            print("?")
    def returnWalmartPrice(self):
        return walmartPrice().floatPrice #not returning correct price (returning 4.63 for the nuts and 14.15 for drink )
        