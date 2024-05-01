#scraping amazon liquid freezers 

# Imports
import requests  # Imports library for HTTP requests
from bs4 import BeautifulSoup as bs  # Imports BeautifulSoup for HTML parsing
import os  # Imports library to interact with the operating system
# End of imports

max_elements = 3  # set a max number of links

def dissipator(dissipator_model: str): # dissipator_model is used to search a specified liquid freezer model
    '''This function scrapes Liquid Freezers from amazon and downloads the amazon webpage on the machine'''
    
    info_dissipator = {"name": [], "price": [], "link": []} # creates a dictionary to store the informations
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'} # simulates a browser request
    
    # URL to search artic liquid dissipators
    url = f"https://www.amazon.it/s?k=arctic+liquid+freezer+{dissipator_model}"
    title_name_check = 'arctic liquid freezer'

    response = requests.get(url, headers=HEADERS) # makes a HTTP request to the URL
    soup = bs(response.content, 'html.parser') # Analyzes the response

    # saving HTML content to analyze it on the machine
    current_dir = os.path.dirname(__file__)
    dissipator_name = f"amazon_arctic_{dissipator_model}.html"
    file_path = os.path.join(current_dir, dissipator_name)
    
    # If the file exists deletes it
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

        if title_name_check.lower() in title.lower() and dissipator_model.lower() in title.lower(): # this if saves only the infos of the requested product
            info_dissipator['name'].append(title)
            info_dissipator['price'].append(price)
            info_dissipator['link'].append(product_url)

    if os.path.exists(file_path):
        os.remove(file_path)
    return info_dissipator

'''dissipator('420')
dissipatore = dissipator('420')
print(f'titolo pagina dissipatore: {dissipatore['name']}')'''