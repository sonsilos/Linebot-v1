from urllib.request import urlopen
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.checkraka.com/econ/stock/'

# query the website and return the html to the variable 'page'
page = urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

#  SET Summary 
set_box = soup.find('div', attrs={'class': 'econ_stock_set_set_summary'})

name = set_box.text.strip(' \t\n\r') # strip() is used to remove starting and trailing
print (name)

# SET Top Value
top_value_box = soup.find('div', attrs={'class':'econ_stock_set_set_value'})
top_value = top_value_box.text.strip(' \t\n\r')
print (top_value)

# SET Top Volume
top_volume_box = soup.find('div', attrs={'class':'econ_stock_set_set_volume'})
top_volume = top_volume_box.text.strip(' \t\n\r')
print (top_volume)

# SET Top Gain
top_gain_box = soup.find('div', attrs={'class':'econ_stock_set_set_gain'})
top_gain = top_gain_box.text.strip(' \t\n\r')
print (top_gain)