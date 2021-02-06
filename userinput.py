# from walmartPrice import *
# from amazonPrice import * 
from selBs4 import *
from prices import * 

bc_input = input("Enter barcode...")
print(bc_input)

start = time.time()

a = prices(bc_input).amazon()
w = prices(bc_input).walmart()
e = prices(bc_input).ebay()

lowestPrice = min(a, w, e)
print("--- %s seconds ---" % (time.time() - start))
print("Patched price is $" + str(lowestPrice))
