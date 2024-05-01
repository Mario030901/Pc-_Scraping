#scraping amazon cases 

# Imports
import requests  # Imports library for HTTP requests
from bs4 import BeautifulSoup as bs  # Imports BeautifulSoup for HTML parsing
import os  # Imports library to interact with the operating system
# End of imports

max_elements = 3  # set a max number of links

def case(case_model: str): # case_model is used to search a specified case model
    '''This function scrapes Corsair cases from amazon and downloads the amazon webpage on the machine'''
    
    case_models=case_model.split(" ")
    info_case = {"name": [], "price": [], "link": []} # creates a dictionary to store the informations
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'} # simulates a browser request
    
    # URL to search corsair cases
    url = f"https://www.amazon.it/s?k=case_corsair+{case_model}"
    title_name_check = 'case corsair'

    response = requests.get(url, headers=HEADERS) # makes a HTTP request to the URL
    soup = bs(response.content, 'html.parser') # Analyzes the response

    # saving HTML content to analyze it on the machine
    current_dir = os.path.dirname(__file__)
    case_name = f"amazon_corsair_{case_model}.html"
    file_path = os.path.join(current_dir, case_name)
    
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

        if title_name_check.lower() in title.lower() and case_models[0].lower() in title.lower() and case_models[1].lower() in title.lower(): # this if saves only the infos of the requested product
            info_case['name'].append(title)
            info_case['price'].append(price)
            info_case['link'].append(product_url)

    return info_case

#case('crystal 570X')