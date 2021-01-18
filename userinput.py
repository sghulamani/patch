# from walmartPrice import *
# from amazonPrice import * 
from selBs4 import *
from returnpricesuseinput import * 

bcinput = input("Enter barcode...")
bc ="'" + bcinput + "'"
print(bc)

returnpricesuseinput(bc).returnAmazonPrice()
returnpricesuseinput(bc).returnWalmartPrice()

