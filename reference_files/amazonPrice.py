from selBs4 import *
class amazonPrice:
    soup2 = selBs4('060549008080','https://www.amazon.ca/s?k=').returnsoup()
    floatPrice = -1
    for item in soup2.find("span", {"class": "a-offscreen"}):
        priceTag= str(item)
        if "$" in priceTag:
            indexSign = priceTag.find("$")
            floatPrice = float(priceTag[indexSign+1:].replace("</span>","")) 
        else:
            print("?")
    def returnAmazonPrice(self):
        return amazonPrice().floatPrice





# https://www.amazon.ca/s?k=B07KXTZ6Q3
# https://www.amazon.ca/s?k=9781338556216
# https://www.amazon.ca/s?k=