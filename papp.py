from flask import Flask, render_template
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import re

# app = Flask(__name__)

bc = '029000020764'
URL = 'https://www.walmart.com/search/?query=' + bc


page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

match = soup.find_all('span', string=re.compile("$"))
print(match)

match01 = soup.find('div', class_="js-content")
match0 = soup.find('div', class_="search-result-productprice listview enable-2price-2")
match = soup.find('span', class_="visuallyhidden")
print(match)
print(match0)
print(match01)

#SELF ATTEMPT
#Beautiful Soup
# page = requests.get(URL).text
# # print(page)
# lookingfor = "$"
# for c in range(0, len(page)):
#     if page[c] == lookingfor:
#         print(5+10)


# print(type(page))

# price = re.findall(r"$[^]]+", matches)

# soup = BeautifulSoup(page.content, 'html.parser')

# matches = soup.find_all("span", class_="visuallyhidden") 
# print(matches)

#Run the app
# @app.route('/') # Rerpites to original website if /____ doesnt exist
# def index():
#     return render_template("website.html")
    
# if __name__ == "__main__":
#     app.run(debug=True, host="localhost")

