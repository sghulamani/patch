from selBs4 import selBs4

class pricescanada:

    def __init__(self, bc):
        self.bc = bc 
    def amazon(self):
        soup = selBs4('https://www.amazon.ca/s?k=' + self.bc).returnsoup()
        for item in soup.find_all("span", {"class": "a-size-mini a-link-normal a-text-normal"}):
            priceTag= str(item)
            if "$" in priceTag:
                indexSign = priceTag.find("$")
                floatPrice = float(priceTag[indexSign+1:].replace("</span>","")) 
                print("the price is $" + str(floatPrice))
                return floatPrice
            else:
                print("?")

    def walmart(self):
        soup = selBs4('https://www.walmart.ca/search/?query=' + self.bc).returnsoup()
        for item in soup.find_all("span", {"class": "visuallyhidden"}):
            priceTag= str(item)
            if "$" in priceTag:
                indexSign = priceTag.find("$")
                floatPrice = float(priceTag[indexSign+1:].replace("</span>","")) 
                print("the price is $" + str(floatPrice))
                return floatPrice
            else:
                print("?")

    def ebay(self):
        soup = selBs4('https://www.ebay.ca/sch/i.html?_from=R40&_nkw=' + self.bc + "&_sop=15").returnsoup()
        for item in soup.find_all("span", {"class": "s-item__price"}):
            priceTag= str(item)
            if "$" in priceTag:
                indexSign = priceTag.find("$")
                floatPrice = float(priceTag[indexSign+1:].replace("</span>","")) 
                print("the price is $" + str(floatPrice))
                return floatPrice
            else:
                print("?")              
            
