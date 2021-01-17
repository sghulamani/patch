from flask import Flask, render_template
from bs4 import BeautifulSoup

import requests
import re


# app = Flask(__name__)


bc = '029000020764'
URL = 'https://www.walmart.com/search/?query=' + bc


page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

match = soup.find_all('span', string=re.compile("$"))
print(match)

matches = soup.find_all("span", class_="visuallyhidden", string=re.compile('$')) 
print(matches)

#Beautiful Soup

# print(type(page))

# price = re.findall(r"$[^]]+", matches)

# soup = BeautifulSoup(page.content, 'html.parser')


#Run the app
# @app.route('/') # Rerpites to original website if /____ doesnt exist
# def index():
#     return render_template("website.html")
    
# if __name__ == "__main__":
#     app.run(debug=True, host="localhost")

