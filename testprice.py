from returnpricesuseinput import *

finalWalmartPrice= returnpricesuseinput(bc).returnWalmartPrice()
print("The price on walmart is $" + str(finalWalmartPrice))

finalAmazonPrice = returnpricesuseinput().returnAmazonPrice()
print("The price on amazon is $" + str(finalAmazonPrice))
