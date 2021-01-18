from flask import Flask, render_template
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
# app = Flask(__name__)

PATH = "C:\Program Files (x86)\chromedriver.exe" 

chrome_options = Options()
ua = UserAgent(use_cache_server = False, verify_ssl=False)
userAgent = ua.random
print(userAgent)
chrome_options.add_argument(f'user-agent={userAgent}')
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(PATH, options=chrome_options)
bc = '029000020764'
URL = 'https://www.walmart.com/search/?query=' + bc
driver.get(URL)
timeout = 60
try:
    time.sleep(0.25)
    element_present = EC.presence_of_element_located((By.ID, 'global-search-input'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out")

soup = BeautifulSoup(driver.page_source,"html.parser")
driver.quit()

for item in soup.find_all("span", {"class": "visuallyhidden"}):
    priceTag= str(item)
    if "$" in priceTag:
        print(priceTag)
        indexPrice = priceTag.find("$")
        intPrice = float(priceTag[indexPrice+1:].replace("</span>","")) 
        print(type(intPrice))
        print(intPrice)
        break


# #Run the app
# @app.route('/') # Rerpites to original website if /____ doesnt exist
# def index():
#     return render_template("website.html")
    
# if __name__ == "__main__":
#     app.run(debug=True, host="localhost")

