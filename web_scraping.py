from urllib.request import urlopen
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.settrade.com/C04_01_stock_quote_p1.jsp?txtSymbol=HUMAN'

# query the website and return the html to the variable 'page'
page = urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
name_box = soup.find('div', attrs={'class': 'round-border'})

name = name_box.text.strip(' \t\n\r') # strip() is used to remove starting and trailing
print (name)

# get the index price
# price_box = soup.find('span', attrs={'class':'text-red'})
# price = price_box.text
# print (price)