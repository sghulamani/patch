from selBs4 import selBs4

class prices:

    def __init__(self, bc):
        self.bc = bc 
    def amazon(self):
        soup = selBs4('https://www.amazon.com/s?k=' + self.bc).returnsoup()
        for item in soup.find_all("span", {"class": "a-offscreen"}):
            priceTag= str(item)
            if "$" in priceTag:
                indexSign = priceTag.find("$")
                floatPrice = float(priceTag[indexSign+1:].replace("</span>","")) 
                print("the price is $" + str(floatPrice))
                return floatPrice

    def walmart(self):
        soup = selBs4('https://www.walmart.com/search/?query=' + self.bc).returnsoup()
        for item in soup.find_all("span", {"class": "visuallyhidden"}):
            priceTag= str(item)
            if "$" in priceTag:
                indexSign = priceTag.find("$")
                floatPrice = float(priceTag[indexSign+1:].replace("</span>","")) 
                print("the price is $" + str(floatPrice))
                return floatPrice

    def ebay(self):
        soup = selBs4('https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + self.bc + "&_sop=15").returnsoup()
        for item in soup.find_all("span", {"class": "s-item__price"}):
            priceTag= str(item)
            if "$" in priceTag:
                indexSign = priceTag.find("$")
                floatPrice = float(priceTag[indexSign+1:].replace("</span>","")) 
                print("the price is $" + str(floatPrice))
<<<<<<< HEAD
                return floatPrice
            else:
                print("?")              
=======
                return floatPrice   
            
>>>>>>> 08475c74ba707803b63b3e23450f4115f2bbe0c0
            
