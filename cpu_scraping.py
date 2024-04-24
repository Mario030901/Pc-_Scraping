#scraping amazon processori 

# Imports
import requests  # Imports library for HTTP requests
from bs4 import BeautifulSoup as bs  # Imports BeautifulSoup for HTML parsing
import os  # Imports library to interact with the operating system
import locale  # Importa il modulo per gestire le impostazioni locali (come la formattazione dei numeri)
limite_elementi = 5  # Imposta un limite per il numero di prodotti da elaborare
media = None  # Inizializza una variabile per memorizzare la media dei prezzi
def processori_amazon_intel(model):
    info = {"nome": [], "prezzo": [], "link": []}
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
    
    # Costruzione URL per la ricerca dei processori Intel
    url = f"https://www.amazon.it/s?k=intel+core+{model}"

    response = requests.get(url, headers=HEADERS)
    soup = bs(response.content, 'html.parser')

    # Salvataggio del contenuto HTML per analisi offline (opzionale)
    current_dir = os.path.dirname(__file__)
    filename = f"amazon_intel_{model}.html"
    filepath = os.path.join(current_dir, filename)
    
    if os.path.exists(filepath):
        os.remove(filepath)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
    
    # Analisi del file HTML salvato per estrarre informazioni sui prodotti
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = bs(file, 'html.parser')
    
    links = soup.find_all('a', attrs={'class': 'a-link-normal s-no-outline'})
    links_list = [link.get('href') for link in links[:5]]  # Limit to first 5 elements

    for link in links_list:
        product_url = "https://www.amazon.it" + link
        product_page = requests.get(product_url, headers=HEADERS)
        product_soup = bs(product_page.content, 'html.parser')
        
        title = product_soup.find('span', attrs={'id': 'productTitle'}).get_text(strip=True)
        try:
            price = product_soup.find('span', attrs={'class': 'a-offscreen'}).get_text(strip=True)
        except AttributeError:
            price = "N/A"

        info['nome'].append(title)
        info['prezzo'].append(price)
        info['link'].append(product_url)

    return info