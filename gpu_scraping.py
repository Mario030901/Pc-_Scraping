# Scraping amazon GPUs 

# Imports
import requests  # Imports library for HTTP requests
from bs4 import BeautifulSoup as bs  # Imports BeautifulSoup for HTML parsing
import os  # Imports library to interact with the operating system
#import locale  # Imports library to manage local settings (for example numbers formatting)
# End of imports

max_elements = 3  # set a max number of links
 
def amazon_gpus(gpu_model: str): # gpu_model is used to search a specified GPU model
    '''This function scrapes GPUs from amazon'''
    info_gpu = {"name" : [], "price" : [], "link" : []}  # creates a dictionary to store the informations
    HEADERS = ({'User-Agent': '...'})  # Imposta un User-Agent per simulare una richiesta da browser
    
    url = "https://www.amazon.it/s?k=rtx+" + str(gpu_model)  # Crea l'URL per la ricerca
    
    response = requests.get(url, headers=HEADERS)  # Makes a HTTP request to the UR
    soup = bs(response.content, "html.parser")  # Analyzes the response

    # saving HTML content to analyze it on the machine
    current_dir = os.path.dirname(__file__)
    gpu_name = "amazon_rtx" + str(gpu_model) + ".html"
    file_path = os.path.join(current_dir, gpu_name)

    # If the file exists deletes it and resaves it
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} has been deleted.")

    # Saving the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
        
    # Analysis of the saved HTML file  to get products infos
    with open(file_path, "r", encoding="utf-8") as htmlfile:
        soup = bs(htmlfile, "html.parser")
        
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

        info_gpu['name'].append(title)
        info_gpu['price'].append(price)
        info_gpu['link'].append(product_url)
        print(info_gpu)

#amazon_gpus('4070')