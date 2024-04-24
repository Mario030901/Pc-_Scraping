#BOZZA INIZIALE 

#inizio dichiarazioni

import requests  # Importa il modulo per fare richieste HTTP
from bs4 import BeautifulSoup as bs  # Importa BeautifulSoup per il parsing HTML
import os  # Importa il modulo per interagire con il sistema operativo
import locale  # Importa il modulo per gestire le impostazioni locali (come la formattazione dei numeri)
limite_elementi = 5  # Imposta un limite per il numero di prodotti da elaborare
media = None  # Inizializza una variabile per memorizzare la media dei prezzi

#all'inizio dobbiamo aggiungere tutta la parte di domanda all'utente di come vuole fare il pc e quanti soldi ha per fare la build 




#funzione scraping per amazon di schede video 
def schede_video_amazon(scheda):
    info_schede = {"nome" : [], "prezzo" : [], "link" : []}  # Dizionario per raccogliere informazioni
    index = 1  # Indice usato per iterare (non usato nel codice fornito)
    HEADERS = ({'User-Agent': '...'})  # Imposta un User-Agent per simulare una richiesta da browser
    
    url = "https://www.amazon.it/s?k=rtx+" + str(scheda)  # Crea l'URL per la ricerca
    
    webpage = requests.get(url, headers=HEADERS)  # Fa una richiesta HTTP all'URL
    soup = bs(webpage.content, "html.parser")  # Analizza il contenuto HTML

    # Percorso dove salvare il file HTML scaricato
    current_dir = os.path.dirname(__file__)
    nome_scheda = "amazon_rtx" + str(scheda) + ".html"
    file_path = os.path.join(current_dir, nome_scheda)

    # Controlla se il file esiste già e in tal caso lo elimina
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Il file {file_path} è stato eliminato.")
    else:
        print(f"Il file {file_path} non esiste.")

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
            if elementi_aggiunti >= limite_elementi:
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