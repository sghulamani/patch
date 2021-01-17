#Beautiful Soup
bc = '029000020764'
URL = 'https://www.walmart.com/search/?query=' + bc
page = requests.get(URL)
print(URL)
soup = BeautifulSoup(page.content, 'html.parser')

price = soup.find(class_="price-group")
print(price)

def getprice(URL):
    price = 3

    return price