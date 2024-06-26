# Scraping amazon RAMs

# Imports
import requests # Imports library for HTTP requests
from bs4 import BeautifulSoup as bs # Imports BeautifulSoup for HTML parsing
import os # Imports library to interact with the operating system
# End of imports

def ram(ram_model: str, ram_hz: str): # ram_model is used to search a specified GPU model, ram_hz tells us the preferred hz of the ram
    '''This function scrapes RAM modules from Amazon and saves the webpage for analysis.'''
    if " " in ram_model:
        ram_model.replace(" ","")
    info_ram = {"name": [], "price": [], "link": []} # creates a dictionary to store the informations
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'} # simulates a browser request
    
    # URL to search RAM modules
    url = f"https://www.amazon.it/s?k=CORSAIR+VENGEANCE+{ram_model}" # URL to search RAMs
    title_name_check = 'corsair vengeance'

    response = requests.get(url, headers=HEADERS) # Makes a HTTP request to the URL
    soup = bs(response.content, 'html.parser') # Analyzes the response

    # Saving HTML content to analyze it on the machine
    current_dir = os.path.dirname(__file__)
    ram_name = f"amazon_ram_{ram_model}.html"
    file_path = os.path.join(current_dir, ram_name)
    
    # If the file exists deletes it and resaves it
    if os.path.exists(file_path):
        os.remove(file_path)

    # Saving the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

    # Analysis of the saved HTML file  to get products infos
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = bs(file, 'html.parser')

    links = soup.find_all('a', attrs={'class': 'a-link-normal s-no-outline'})
    links_list = [link.get('href') for link in links[:3]]  # Limit to first 3 elements

    # Download of the page and info extraction for every product
    for link in links_list:
        product_url = "https://www.amazon.it" + link
        product_page = requests.get(product_url, headers=HEADERS)
        product_soup = bs(product_page.content, 'html.parser')

        title = product_soup.find('span', attrs={'id': 'productTitle'}).get_text(strip=True)
        try:
            price = product_soup.find('span', attrs={'class': 'a-offscreen'}).get_text(strip=True)
        except AttributeError:
            price = "N/A"

        if title_name_check.lower() in title.lower() and ram_model.lower() in title.lower() and ram_hz.lower() in title.lower(): # this if saves only the infos of the requested product
            info_ram['name'].append(title)
            info_ram['price'].append(price)
            info_ram['link'].append(product_url)

    if os.path.exists(file_path):
        os.remove(file_path)
    return info_ram

def find_cheapest(ram_infos: dict):
    '''This function searches for the cheapest RAM amongst the ones collected from the scraping'''
    cheapest_ram = {}
    cont=0
    for i in zip(ram_infos["price"], ram_infos["link"]):
        if cont==0:
            cheapest_ram["price"]=i[0]
            cheapest_ram["link"]=i[1]
        else:
            if cheapest_ram["price"]>i[0]: 
                cheapest_ram["price"] = i[0]
                cheapest_ram["link"]=i[1]
        cont+=1
    return cheapest_ram

def download_file(cheapest_ram: dict):
    '''This function downloads on the machine the webpage of the cheapest RAM'''
    # Saving the file
    print("downloading RAM file")
    current_dir = os.path.dirname(__file__)
    ram_file = f"cheapest_ram.html"
    ram_file_path = os.path.join(current_dir, ram_file)
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'} # simulates a browser request
    response = requests.get(cheapest_ram["link"], headers=HEADERS) # makes a HTTP request to the URL
    soup = bs(response.content, 'html.parser') # Analyzes the response
    # If the file exists deletes it
    if os.path.exists(ram_file_path):
        os.remove(ram_file_path)
    with open(ram_file_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

#ram("16gb")