# from walmartPrice import *
# from amazonPrice import * 
from selBs4 import *
from returnpricesuseinput import * 

bcinput = input("Enter barcode...")
bc = bcinput
print(bc)




lowestPrice = min(returnpricesuseinput(bc).returnAmazonPrice(), returnpricesuseinput(bc).returnWalmartPrice(), returnpricesuseinput(bc).returneBayPrice())
print("Patched price is $" + str(lowestPrice))
