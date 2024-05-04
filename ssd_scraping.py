# Scraping amazon SSDs 

# Imports
import requests  # Imports library for HTTP requests
from bs4 import BeautifulSoup as bs  # Imports BeautifulSoup for HTML parsing
import os  # Imports library to interact with the operating system
# End of imports

def amazon_ssd(ssd_model: str): # ssd_model is used to search a specified GPU model
    '''This function scrapes SSDs from amazon and downloads the amazon webpage on the machine'''
    if " " in ssd_model:
        ssd_models=ssd_model.split(" ")
        info_ssd = {"name" : [], "price" : [], "link" : []}  # creates a dictionary to store the informations
        HEADERS = ({'User-Agent': '...'})  # simulates a browser request
        
        url = "https://www.amazon.it/s?k=internal+ssd+" + str(ssd_model)  # URL to search SSDs
        title_name_check = 'ssd'
        
        response = requests.get(url, headers=HEADERS)  # Makes a HTTP request to the URL
        soup = bs(response.content, "html.parser")  # Analyzes the response

        # saving HTML content to analyze it on the machine
        current_dir = os.path.dirname(__file__)
        ssd_name = "amazon_Samsung" + str(ssd_model) + ".html"
        file_path = os.path.join(current_dir, ssd_name)

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

            if title_name_check.lower() in title.lower() and ssd_models[0].lower() in title.lower() and ssd_models[1].lower() in title.lower(): # this if saves only the infos of the requested product
                info_ssd['name'].append(title)
                info_ssd['price'].append(price)
                info_ssd['link'].append(product_url)
    else:
        info_ssd = {"name" : [], "price" : [], "link" : []}  # creates a dictionary to store the informations
        HEADERS = ({'User-Agent': '...'})  # simulates a browser request
        
        url = "https://www.amazon.it/s?k=ssd+" + str(ssd_model)  # URL to search SSDs
        title_name_check = 'ssd'
        
        response = requests.get(url, headers=HEADERS)  # Makes a HTTP request to the URL
        soup = bs(response.content, "html.parser")  # Analyzes the response

        # saving HTML content to analyze it on the machine
        current_dir = os.path.dirname(__file__)
        ssd_name = "amazon_Samsung" + str(ssd_model) + ".html"
        file_path = os.path.join(current_dir, ssd_name)

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

            if title_name_check.lower() in title.lower() and ssd_model.lower() in title.lower(): # this if saves only the infos of the requested product
                info_ssd['name'].append(title)
                info_ssd['price'].append(price)
                info_ssd['link'].append(product_url)

    if os.path.exists(file_path):
        os.remove(file_path)
    return info_ssd

def find_cheapest(ssd_infos: dict):
    
    cheapest_ssd = {}
    cont=0
    print("downloading SSD file")
    for i in zip(ssd_infos["price"], ssd_infos["link"]):
        if cont==0:
            cheapest_ssd["price"]=i[0]
            cheapest_ssd["link"]=i[1]
        else:
            if cheapest_ssd["price"]>i[0]: 
                cheapest_ssd["price"] = i[0]
                cheapest_ssd["link"]=i[1]
        cont+=1
    return cheapest_ssd

def download_file(cheapest_ssd: dict):
    
    # Saving the file
    current_dir = os.path.dirname(__file__)
    ssd_file = f"cheapest_ssd.html"
    ssd_file_path = os.path.join(current_dir, ssd_file)
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'} # simulates a browser request
    response = requests.get(cheapest_ssd["link"], headers=HEADERS) # makes a HTTP request to the URL
    soup = bs(response.content, 'html.parser') # Analyzes the response
    # If the file exists deletes it
    if os.path.exists(ssd_file_path):
        os.remove(ssd_file_path)
    with open(ssd_file_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

#amazon_ssd('1T')