from bs4 import BeautifulSoup
import requests

source = requests.get('https://stuff.co.nz').text
source = requests.get('https://www.stuff.co.nz/business/property/124125670/russian-billionaire-investing-in-kiwibuild-to-help-housing-crisis').text

soup = BeautifulSoup(source, 'html')

print(soup.prettify())