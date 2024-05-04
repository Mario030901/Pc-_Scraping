#scraping amazon power supply 

# Imports
import requests  # Imports library for HTTP requests
from bs4 import BeautifulSoup as bs  # Imports BeautifulSoup for HTML parsing
import os  # Imports library to interact with the operating system
# End of imports

def pws(pws_model: str):   # power supply model is used to search a specified CPU model
    
    info_pws = {"name": [], "price": [], "link": []}
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
    
    # URL to search power supplies
    url = f"https://www.amazon.it/s?k=power+supply+corsair{pws_model}"
    title_name_check = 'corsair'

    response = requests.get(url, headers=HEADERS)  # makes a HTTP request to the URL
    soup = bs(response.content, 'html.parser')  # Analyzes the response

    # Saving HTML content to analyze it on the machine
    current_dir = os.path.dirname(__file__)
    psu_name = f"amazon_pws_{pws_model}.html"
    file_path = os.path.join(current_dir, psu_name)
    
     # If the file exists deletes it
    if os.path.exists(file_path):
        os.remove(file_path)

    # Saving the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

     # Analysis of the saved HTML file  to get products infos
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = bs(file, 'html.parser')

    # Download of the page and info extraction for every product
    links = soup.find_all('a', attrs={'class': 'a-link-normal s-no-outline'})
    links_list = [link.get('href') for link in links[:5]]  # Limit to first 3 elements

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

        if title_name_check.lower() in title.lower() and pws_model.lower() in title.lower():  # this if saves only the infos of the requested product
            info_pws['name'].append(title)
            info_pws['price'].append(price)
            info_pws['link'].append(product_url)
            
    if os.path.exists(file_path):
        os.remove(file_path)
    return info_pws

def find_cheapest(pws_infos: dict):
    '''This function searches for the cheapest POWER SUPPLY amongst the ones collected from the scraping'''
    cheapest_pws = {}
    cont=0
    print("downloading POWER SUPPLY file")
    for i in zip(pws_infos["price"], pws_infos["link"]):
        if cont==0:
            cheapest_pws["price"]=i[0]
            cheapest_pws["link"]=i[1]
        else:
            if cheapest_pws["price"]>i[0]: 
                cheapest_pws["price"] = i[0]
                cheapest_pws["link"]=i[1]
        cont+=1
    return cheapest_pws

def download_file(cheapest_pws: dict):
    '''This function downloads on the machine the webpage of the cheapest POWER SUPPLY'''
    # Saving the file
    current_dir = os.path.dirname(__file__)
    pws_file = f"cheapest_powerSupply.html"
    pws_file_path = os.path.join(current_dir, pws_file)
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'} # simulates a browser request
    response = requests.get(cheapest_pws["link"], headers=HEADERS) # makes a HTTP request to the URL
    soup = bs(response.content, 'html.parser') # Analyzes the response
    # If the file exists deletes it
    if os.path.exists(pws_file_path):
        os.remove(pws_file_path)
    with open(pws_file_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

# Example usage
# pws_amazon('650W')