from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


# app = Flask(__name__)

#Beautiful Soup
bc = '029000020764'
URL = 'https://www.walmart.com/search/?query=' + bc
page = requests.get(URL)
print(URL)
soup = BeautifulSoup(page.content, 'html.parser')

price = soup.find(class_="price-group")
print(price)

#Run the app
# @app.route('/') # Rerpites to original website if /____ doesnt exist
# def index():
#     return render_template("website.html")
    
# if __name__ == "__main__":
#     app.run(debug=True, host="localhost")

