#scraping amazon power supply 

# Imports
import requests  # Imports library for HTTP requests
from bs4 import BeautifulSoup as bs  # Imports BeautifulSoup for HTML parsing
import os  # Imports library to interact with the operating system
# End of imports

max_elements = 3  # set a max number of links

def pws(pws_model: str):   # power supply model is used to search a specified CPU model
    
    info_pws = {"name": [], "price": [], "link": []}
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
    
    # URL to search power supplies
    url = f"https://www.amazon.it/s?k=power+supply+corsair{pws_model}"
    title_name_check = 'power supply corsair'

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

        if title_name_check.lower() in title.lower() and pws_model.lower() in title.lower():  
            info_pws['name'].append(title)
            info_pws['price'].append(price)
            info_pws['link'].append(product_url)

    return info_pws

# Example usage
# psu_amazon('650W')