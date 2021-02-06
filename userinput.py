
from selBs4 import *
from prices import * 
from pricescanada import *


region_input = " "
while(region_input != "canada" or "us" ):
    region_input = input("Enter region (Canada or US)...")    #CANDA REGION HASMORE ADS SO YOU NEED TO REFER TO THE LINK AND BARCODE TO GET DATA
    if (region_input == "canada" or "us"):
        region_input = region_input.lower()
        print(region_input)
        if (region_input == "canada"):
            bc_input = input("Enter barcode...")
            a = pricescanada(bc_input).amazon()
            # w = pricescanada(bc_input).walmart() 
            # e = pricescanada(bc_input).ebay()
            break

        if(region_input == "us"):
            bc_input = input("Enter barcode...")
            a = prices(bc_input).amazon()
            # w = prices(bc_input).walmart() 
            # e = prices(bc_input).ebay()
            break
    

# start = time.time()

lowestPrice = min(a)   # w is removed
# end = time.time()
# total = end - start
print("Total time taken  " + str(total))
print("Patched price is $" + str(lowestPrice))


# test upc 9781338556216