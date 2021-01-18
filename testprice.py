from amazonPrice import *
from walmartPrice import *

finalWalmartPrice= walmartPrice().returnWalmartPrice()
print("The price on walmart is $" + str(finalWalmartPrice))

finalAmazonPrice = amazonPrice().returnAmazonPrice()
print("The price on amazon is $" + str(finalAmazonPrice))

if (finalAmazonPrice > finalWalmartPrice):
    print("The price for walmart is best!")
else:
    print("The price for amazon is best!")