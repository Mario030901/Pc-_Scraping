# Scraping amazon GPUs 

# Imports
import requests  # Imports library for HTTP requests
from bs4 import BeautifulSoup as bs  # Imports BeautifulSoup for HTML parsing
import os  # Imports library to interact with the operating system
# End of imports

def gpu(gpu_model: str): # gpu_model is used to search a specified GPU model
    '''This function scrapes GPUs from amazon and downloads the amazon webpage on the machine'''
    if " " in gpu_model:
        gpu_models=gpu_model.split(" ")
        info_gpu = {"name" : [], "price" : [], "link" : []}  # creates a dictionary to store the informations
        HEADERS = ({'User-Agent': '...'})  # simulates a browser request
    
        url = "https://www.amazon.it/s?k=rtx+" + str(gpu_model)  # URL to search Intel cpus
        title_name_check = 'rtx'
    
        response = requests.get(url, headers=HEADERS)  # Makes a HTTP request to the UR
        soup = bs(response.content, "html.parser")  # Analyzes the response

        # saving HTML content to analyze it on the machine
        current_dir = os.path.dirname(__file__)
        gpu_name = "amazon_rtx" + str(gpu_model) + ".html"
        file_path = os.path.join(current_dir, gpu_name)

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

            if title_name_check.lower() in title.lower() and gpu_models[0].lower() in title.lower() and gpu_models[1].lower() in title.lower(): # this if saves only the infos of the requested product
                info_gpu['name'].append(title)
                info_gpu['price'].append(price)
                info_gpu['link'].append(product_url)
    else: 
        info_gpu = {"name" : [], "price" : [], "link" : []}  # creates a dictionary to store the informations
        HEADERS = ({'User-Agent': '...'})  # simulates a browser request

        url = "https://www.amazon.it/s?k=rtx+" + str(gpu_model)  # URL to search Intel cpus
        title_name_check = 'rtx'

        response = requests.get(url, headers=HEADERS)  # Makes a HTTP request to the UR
        soup = bs(response.content, "html.parser")  # Analyzes the response

        # saving HTML content to analyze it on the machine
        current_dir = os.path.dirname(__file__)
        gpu_name = "amazon_rtx" + str(gpu_model) + ".html"
        file_path = os.path.join(current_dir, gpu_name)

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

            if title_name_check.lower() in title.lower() and gpu_model.lower() in title.lower(): # this if saves only the infos of the requested product
                info_gpu['name'].append(title)
                info_gpu['price'].append(price)
                info_gpu['link'].append(product_url)

    if os.path.exists(file_path):
        os.remove(file_path)
    return info_gpu

def find_cheapest(gpu_infos: dict):
    '''This function searches for the cheapest GPU amongst the ones collected from the scraping'''
    cheapest_gpu = {}
    cont = 0
    for i in zip(gpu_infos["price"], gpu_infos["link"]):
        if cont==0:
            cheapest_gpu["price"]=i[0]
            cheapest_gpu["link"]=i[1]
        else:
            if cheapest_gpu["price"]>i[0]:
                cheapest_gpu["price"] = i[0]
                cheapest_gpu["link"]=i[1]
        cont+=1
    return cheapest_gpu

def download_file(cheapest_gpu: dict):
    '''This function downloads on the machine the webpage of the cheapest GPU'''
    # Saving the file
    print("downloading GPU file")
    current_dir = os.path.dirname(__file__)
    gpu_file = f"cheapest_gpu.html"
    gpu_file_path = os.path.join(current_dir, gpu_file)
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'} # simulates a browser request
    response = requests.get(cheapest_gpu["link"], headers=HEADERS) # makes a HTTP request to the URL
    soup = bs(response.content, 'html.parser') # Analyzes the response
    # If the file exists deletes it
    if os.path.exists(gpu_file_path):
        os.remove(gpu_file_path)
    with open(gpu_file_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

#gpu('4070')