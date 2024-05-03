# Scraping amazon Mother Boards 

# Imports
import requests  # Imports library for HTTP requests
from bs4 import BeautifulSoup as bs  # Imports BeautifulSoup for HTML parsing
import os  # Imports library to interact with the operating system
# End of imports

def amazon_mother_boards(mb_model: str): # mb_model is used to search a specified GPU model
    '''This function scrapes Mother Boards from amazon and downloads the amazon webpage on the machine'''
    if " " in mb_model:
        mb_models=mb_model.split(" ")
        info_mb = {"name" : [], "price" : [], "link" : []}  # creates a dictionary to store the informations
        HEADERS = ({'User-Agent': '...'})  # simulates a browser request
        
        url = "https://www.amazon.it/s?k=Asus+" + str(mb_model)  # URL to search Intel cpus
        title_name_check = 'asus'
        
        response = requests.get(url, headers=HEADERS)  # Makes a HTTP request to the UR
        soup = bs(response.content, "html.parser")  # Analyzes the response

        # saving HTML content to analyze it on the machine
        current_dir = os.path.dirname(__file__)
        motherboard_name = "amazon_Asus" + str(mb_model) + ".html"
        file_path = os.path.join(current_dir, motherboard_name)

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

            if title_name_check.lower() in title.lower() and mb_models[0].lower() in title.lower() and mb_models[1].lower() in title.lower(): # this if saves only the infos of the requested product
                    info_mb['name'].append(title)
                    info_mb['price'].append(price)
                    info_mb['link'].append(product_url)
    else:
        info_mb = {"name" : [], "price" : [], "link" : []}  # creates a dictionary to store the informations
        HEADERS = ({'User-Agent': '...'})  # simulates a browser request
        
        url = "https://www.amazon.it/s?k=Asus+" + str(mb_model)  # URL to search Intel cpus
        title_name_check = 'asus'
        
        response = requests.get(url, headers=HEADERS)  # Makes a HTTP request to the UR
        soup = bs(response.content, "html.parser")  # Analyzes the response

        # saving HTML content to analyze it on the machine
        current_dir = os.path.dirname(__file__)
        motherboard_name = "amazon_Asus" + str(mb_model) + ".html"
        file_path = os.path.join(current_dir, motherboard_name)

        # If the file exists deletes it and resaves it
        if os.path.exists(file_path):
            os.remove(file_path)

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

            if title_name_check.lower() in title.lower() and mb_model.lower() in title.lower(): # this if saves only the infos of the requested product
                info_mb['name'].append(title)
                info_mb['price'].append(price)
                info_mb['link'].append(product_url)
        
    if os.path.exists(file_path):
        os.remove(file_path)
    return info_mb

#amazon_mother_boards('Z790')