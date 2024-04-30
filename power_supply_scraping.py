import requests
from bs4 import BeautifulSoup as bs
import os

def pws(psu_model: str):
    '''This function scrapes power supplies from Amazon and saves the webpage for analysis.'''
    
    info_psu = {"name": [], "price": [], "link": []}
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
    
    # URL to search power supplies
    url = f"https://www.amazon.it/s?k={psu_model}+power+supply"

    response = requests.get(url, headers=HEADERS)
    soup = bs(response.content, 'html.parser')

    # Saving HTML content to analyze it on the machine
    current_dir = os.path.dirname(__file__)
    psu_name = f"amazon_psu_{psu_model}.html"
    file_path = os.path.join(current_dir, psu_name)
    
    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

    with open(file_path, 'r', encoding='utf-8') as file:
        soup = bs(file, 'html.parser')

    links = soup.find_all('a', attrs={'class': 'a-link-normal s-no-outline'})
    links_list = [link.get('href') for link in links[:3]]  # Limit to first 3 elements

    for link in links_list:
        product_url = "https://www.amazon.it" + link
        product_page = requests.get(product_url, headers=HEADERS)
        product_soup = bs(product_page.content, 'html.parser')

        title = product_soup.find('span', attrs={'id': 'productTitle'}).get_text(strip=True)
        try:
            price = product_soup.find('span', attrs={'class': 'a-offscreen'}).get_text(strip=True)
        except AttributeError:
            price = "N/A"

        info_psu['name'].append(title)
        info_psu['price'].append(price)
        info_psu['link'].append(product_url)

    return info_psu

# Example usage
# psu_amazon('650W')