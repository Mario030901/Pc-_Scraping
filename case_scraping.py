#scraping amazon cases 

# Imports
import requests  # Imports library for HTTP requests
from bs4 import BeautifulSoup as bs  # Imports BeautifulSoup for HTML parsing
import os  # Imports library to interact with the operating system
# End of importsù

def case(case_model: str): # case_model is used to search a specified case model
    '''This function scrapes Corsair cases from amazon and downloads the amazon webpage on the machine'''
    
    if " " in case_model:
        case_models=case_model.split(" ")
        info_case = {"name": [], "price": [], "link": []} # creates a dictionary to store the informations
        HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'} # simulates a browser request
    
        # URL to search corsair cases
        url = f"https://www.amazon.it/s?k=case+corsair+{case_models[0]}+{case_models[1]}"
        title_name_check = 'corsair'

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

            if title_name_check.lower() in title.lower() and case_models[0].lower() in title.lower() and case_models[1].lower() in title.lower(): # this if saves only the infos of the requested product
                info_case['name'].append(title)
                info_case['price'].append(price)
                info_case['link'].append(product_url)
    else:
        info_case = {"name": [], "price": [], "link": []} # creates a dictionary to store the informations
        HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'} # simulates a browser request
    
        # URL to search corsair cases
        url = f"https://www.amazon.it/s?k=case+corsair+{case_model}"
        title_name_check = 'corsair'

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

            if title_name_check.lower() in title.lower() and case_model.lower() in title.lower(): # this if saves only the infos of the requested product
                info_case['name'].append(title)
                info_case['price'].append(price)
                info_case['link'].append(product_url)

    if os.path.exists(file_path):
        os.remove(file_path)
    return info_case

def find_cheapest(case_infos: dict):
    '''This function searches for the cheapest CASE amongst the ones collected from the scraping'''
    cont=0
    cheapest_case = {}
    for i in zip(case_infos["price"], case_infos["link"]):
        if cont==0:
            cheapest_case["price"]=i[0]
            cheapest_case["link"]=i[1]
        else:
            if cheapest_case["price"]>i[0]: 
                cheapest_case["price"] = i[0]
                cheapest_case["link"]=i[1]
        cont+=1
    return cheapest_case

def download_file(cheapest_case: dict):
    '''This function downloads on the machine the webpage of the cheapest CASE'''
    # Saving the file
    print("downloading CASE file")
    current_dir = os.path.dirname(__file__)
    case_file = f"cheapest_case.html"
    case_file_path = os.path.join(current_dir, case_file)
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'} # simulates a browser request
    response = requests.get(cheapest_case["link"], headers=HEADERS) # makes a HTTP request to the URL
    soup = bs(response.content, 'html.parser') # Analyzes the response
    # If the file exists deletes it
    if os.path.exists(case_file_path):
        os.remove(case_file_path)
    with open(case_file_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

#case('crystal 570X')