# Scraping amazon GPUs 

# Imports
import requests  # Imports library for HTTP requests
from bs4 import BeautifulSoup as bs  # Imports BeautifulSoup for HTML parsing
import os  # Imports library to interact with the operating system
#import locale  # Imports library to manage local settings (for example numbers formatting)
# End of imports

max_elements = 3  # set a max number of links
 
def amazon_gpus(gpu_model): # gpu_model is used to search a specified GPU model
    '''This function scrapes GPUs from amazon'''
    info_schede = {"nome" : [], "prezzo" : [], "link" : []}  # creates a dictionary to store the informations
    HEADERS = ({'User-Agent': '...'})  # Imposta un User-Agent per simulare una richiesta da browser
    
    url = "https://www.amazon.it/s?k=rtx+" + str(gpu_model)  # Crea l'URL per la ricerca
    
    response = requests.get(url, headers=HEADERS)  # Makes a HTTP request to the UR
    soup = bs(response.content, "html.parser")  # Analyzes the response

    # Percorso dove salvare il file HTML scaricato
    current_dir = os.path.dirname(__file__)
    nome_scheda = "amazon_rtx" + str(gpu_model) + ".html"
    file_path = os.path.join(current_dir, nome_scheda)

    # Controlla se il file esiste già e in tal caso lo elimina
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} has been deleted.")
    else:
        print(f"File {file_path} doesn't exist.")

    # Salva la nuova pagina HTML
    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(soup.prettify())

    # Riapre il file HTML e fa ulteriori operazioni di parsing
    with open(file_path, "r", encoding="utf-8") as htmlfile:
        soup = bs(htmlfile, "html.parser")
        links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

        links_list = []
        elementi_aggiunti = 0
        for link in links:
            if elementi_aggiunti >= max_elements:
                break
            links_list.append("https://www.amazon.it" + link.get('href'))
            elementi_aggiunti += 1

        # Per ogni link trovato, scarica la pagina del prodotto e estrae le informazioni
        for link in links_list:
            new_webpage = requests.get(link, headers=HEADERS)
            new_soup = bs(new_webpage.content, "html.parser")
            
            try:
                title = new_soup.find("span", attrs={"id": 'productTitle'}).string.strip()
                info_schede["nome"].append(title)
                info_schede["link"].append(link)
            except AttributeError:
                pass  # Gestisce il caso in cui non si trovi il titolo
            
            try:
                price = new_soup.find('span', attrs={'class': 'a-offscreen'}).string.strip()
                info_schede["prezzo"].append(price)
            except AttributeError:
                pass  # Gestisce il caso in cui non si trovi il prezzo

    return info_schede



#Le funzioni akinformatica e nexths sono molto simili a amazon e seguono lo stesso pattern:
#Configurano l'URL e i headers.
#Fanno il download del contenuto HTML.
#Salva il file HTML e lo riapre per il parsing.
#Estraggono i link ai prodotti.
#Per ogni prodotto, estraggono i dettagli (nome, link, prezzo) e li salvano.
