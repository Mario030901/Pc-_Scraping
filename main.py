# Import
import case_scraping as c
import cpu_scraping as cpu
import gpu_scraping as gpu
import liquid_dissipator_scraping as ld
import motherboard_scraping as mb
import ssd_scraping as ssd
import ram_scraping as ram
import power_supply_scraping as pws 
# End of import

print("Before we start please note that we scrape from amazon, so, if you insert a model that doesn't exist you won't get nothing. Be careful")

# Variabili iniziali
controllo = False
gpu_model = ""
cpu_infos={}
scelta = 0
budget = 0
preferenza = ""

# Prima di procedere con la scelta della scheda, chiedi il budget e le preferenze dell'utente
'''try:
    budget = float(input("Insert the PC budget in euro\n"))
    print("Would you prefer a PC more performing in:\n")
    print("(1) GPU - Graphics | (2) CPU - Processor")

    while True:
        preferenza_scelta = int(input())
    
        if preferenza_scelta == 1:
            preferenza = "GPU"
            print("For an optimal GPU, we suggest the 4000 serie of NVIDIA, like RTX 4060, 4070, 4080 or the powerful 4090.")
            break
        elif preferenza_scelta == 2:
            preferenza = "CPU"
            print("For the latest generation CPUs, we suggest 14th generation processors. Note: We know thanks to experience that 13th generation processors tend to overheat.")
            break
        else:
            print("Wrong value, insert 1 or 2 to go on.")
except ValueError as e:
    print(f"Error: {e}")
    exit()

# Ciclo while per la scelta della serie e del modello della scheda video3
try:
     # Chiede all'utente di scegliere tra serie 3000 o 4000 RTX
    scelta = int(input("Insert: (1) to choose serie 3000 RTX | (2) to choose serie 4000 RTX: "))
        
    if scelta == 1:
        while True:
            try:
                print("Insert (50) to choose the 3050 RTX")
                print("Inserisci (60) per scegliere la 3060 RTX")
                print("Inserisci (70) per scegliere la 3070 RTX")
                print("Inserisci (80) per scegliere la 3080 RTX")
                scheda = int(input("Inserisci (90) per scegliere la 3090 RTX: \n"))
                    
                if scheda == 50:
                    scheda = 3050
                    controllo = True
                    break
                
                elif scheda == 60:
                    scheda = 3060
                    controllo = True
                    break
                elif scheda == 70:
                    scheda = 3070
                    controllo = True
                    break
                elif scheda == 80:
                    scheda = 3080
                    controllo = True
                    break
                elif scheda == 90:
                    scheda = 3090
                    controllo = True
                    break
                else:
                    raise ValueError()
            except ValueError:
                print("Inserisci una scheda video valida")
            if controllo:
                break

    elif scelta == 2:
            while True:
                try:
                    print("Inserisci (60) per scegliere la 4060 RTX")
                    print("Inserisci (70) per scegliere la 4070 RTX")
                    print("Inserisci (80) per scegliere la 4080 RTX")
                    scheda = int(input("Inserisci (90) per scegliere la 4090 RTX: \n"))
                
                    if scheda == 60:
                        scheda = 4060
                        controllo = True
                        break
                    elif scheda == 70:
                        scheda = 4070
                        controllo = True
                        break
                    elif scheda == 80:
                        scheda = 4080
                        controllo = True
                        break
                    elif scheda == 90:
                        scheda = 4090
                        controllo = True
                        break
                    else:
                        raise ValueError()
                except ValueError:
                    print("Inserisci una scheda video valida")
                if controllo:
                    break
    else:
            raise ValueError()
except ValueError:
    print("Devi inserire un numero intero valido")
    scelta2 = 0'''
    
# Request of the desired CPU
print("Request of the desired Intel CPU (processor)\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert: i5 14500\n")
    cpu_infos=cpu.cpu(input("insert the desired cpu:\n"))
    if cpu_infos["link"]!=[]:
        print(cpu_infos)
        break
    else: 
        print(cpu_infos)
        print("the desired model doesn't exist on amazon, try something else\n")
    
    
'''while True:  #scelta visualizzazione informazioni
    try:
        print("Che cosa vuoi fare?\n")
        print("(1) Mostra il prezzo più basso | (2) Mostra il prezzo più alto")
        print("(3) Mostra il prezzo medio totale | (4) Mostra tutte le schede video trovate")
        scelta2 = int(input("(5) Per uscire: \n"))
        if scelta2 == 1:
            schede_amazon = pp.amazon(scheda)
            schede_akinformatica = pp.akinformatica(scheda)
            schede_nexths = pp.nexths(scheda)
            nomi_amazon = schede_amazon["nome"]
            nomi_akinformatica = schede_akinformatica["nome"]
            nomi_nexths = schede_nexths["nome"]
            
            #faccio i relativi controlli se ci sono o meno degli
            if not nomi_amazon and not nomi_akinformatica and not nomi_nexths:
                print("Non sono state trovate schede video in vendita \n")
                break

            schede_amazon_checked = {}  # Inizializza schede_amazon_checked come dizionario vuoto
            schede_akinformatica_checked = {}  # Inizializza schede_akinformatica_checked come dizionario vuoto
            schede_nexths_checked = {}  # Inizializza schede_nexths_checked come dizionario vuoto

            if nomi_amazon:
                schede_amazon_checked = pp.check_soglia(schede_amazon)  # controllo soglia prezzi amazon
            
            else:
                print("Non sono state trovate schede video in vendita su Amazon\n")
            if nomi_akinformatica:
                schede_akinformatica_checked = pp.cast_prezzi(pp.akinformatica(scheda)) # controllo soglia prezzi akinformatica

            else:
                 print("Non sono state trovate schede video in vendita su Akinformatica \n")
            if nomi_nexths:
                schede_nexths_checked = pp.cast_prezzi(pp.nexths(scheda))  # controllo soglia prezzi nexths

            else:
                print("Non sono state trovate schede video in vendita su Nexths \n")
            
            prezzo_min = pp.prezzo_basso(schede_amazon_checked, schede_akinformatica_checked, schede_nexths_checked)
            if prezzo_min:
                nome_min = prezzo_min["nome"]
                prezzo_minimo = prezzo_min["prezzo"]
                link_min = prezzo_min["link"]
                print("Prodotto con prezzo minimo:")
                print(f"Nome: {nome_min}")
                print(f"Prezzo: {prezzo_minimo}€")
                print(f"Link: {link_min}")
            else:
                print("Nessun prodotto trovato.")

        elif scelta2 == 2: #prezzo più alto
            schede_amazon = pp.amazon(scheda)
            schede_akinformatica = pp.akinformatica(scheda)
            schede_nexths = pp.nexths(scheda)
            nomi_amazon = schede_amazon["nome"]
            nomi_akinformatica = schede_akinformatica["nome"]
            nomi_nexths = schede_nexths["nome"]

            #faccio i relativi controlli se ci sono o meno degli
            if not nomi_amazon and not nomi_akinformatica and not nomi_nexths:
                print("Non sono state trovate schede video in vendita \n")
                break

            schede_amazon_checked = {}  # Inizializza schede_amazon_checked come dizionario vuoto
            schede_akinformatica_checked = {}  # Inizializza schede_akinformatica_checked come dizionario vuoto
            schede_nexths_checked = {}  # Inizializza schede_nexths_checked come dizionario vuoto

            if nomi_amazon:
                schede_amazon_checked = pp.check_soglia(schede_amazon)  # controllo soglia prezzi amazon
            
            else:
                print("Non sono state trovate schede video in vendita su Amazon\n")
            if nomi_akinformatica:
                schede_akinformatica_checked = pp.cast_prezzi(pp.akinformatica(scheda)) # controllo soglia prezzi akinformatica

            else:
                 print("Non sono state trovate schede video in vendita su Akinformatica \n")
            if nomi_nexths:
                schede_nexths_checked = pp.cast_prezzi(pp.nexths(scheda))  # controllo soglia prezzi nexths

            else:
                print("Non sono state trovate schede video in vendita su Nexths \n")
            
            prezzo_max = pp.prezzo_alto(schede_amazon_checked, schede_akinformatica_checked, schede_nexths_checked)
            if prezzo_max:
                nome_max = prezzo_max["nome"]
                prezzo_massimo = prezzo_max["prezzo"]
                link_max = prezzo_max["link"]
                print("Prodotto con prezzo massimo:")
                print(f"Nome: {nome_max}")
                print(f"Prezzo: {prezzo_massimo}€")
                print(f"Link: {link_max}")
            else:
                print("Nessun prodotto trovato.")

            #faccio i relativi controlli se ci sono o meno degli
            if not nomi_amazon and not nomi_akinformatica and not nomi_nexths:
                print("Non sono state trovate schede video in vendita \n")
                break

            schede_amazon_checked = {}  # Inizializza schede_amazon_checked come dizionario vuoto
            schede_akinformatica_checked = {}  # Inizializza schede_akinformatica_checked come dizionario vuoto
            schede_nexths_checked = {}  # Inizializza schede_nexths_checked come dizionario vuoto

            if nomi_amazon:
                schede_amazon_checked = pp.check_soglia(schede_amazon)  # controllo soglia prezzi amazon
            
            else:
                print("Non sono state trovate schede video in vendita su Amazon\n")
            if nomi_akinformatica:
                schede_akinformatica_checked = pp.cast_prezzi(pp.akinformatica(scheda)) # controllo soglia prezzi akinformatica

            else:
                 print("Non sono state trovate schede video in vendita su Akinformatica \n")
            if nomi_nexths:
                schede_nexths_checked = pp.cast_prezzi(pp.nexths(scheda))  # controllo soglia prezzi nexths

            else:
                print("Non sono state trovate schede video in vendita su Nexths \n")
            
            media = pp.calcola_media_prezzi(schede_amazon_checked, schede_akinformatica_checked, schede_nexths_checked)
            if media:
                print(f"Prezzo medio totale: {media}€")
            else:
                print("Nessun prodotto trovato.")

        elif scelta2 == 4:
            #parte in cui stampo i risultati di amazon
            schede_amazon = pp.amazon(scheda)
            nomi_amazon = schede_amazon["nome"]
            prezzi_amazon = schede_amazon["prezzo"]
            link_amazon = schede_amazon["link"]
            if not nomi_amazon:
                print("Non sono state trovate schede video su amazon \n")
            else:
                print("Schede trovate da amazon \n")
                for nome, prezzo, link in zip(nomi_amazon, prezzi_amazon,link_amazon):
                    print("Nome:", nome)
                    print("Prezzo:", prezzo)
                    print("Link prodotto:", link)
                    print("\n")
            print("--------------------------------------------------------------------------------------------")

            #parte in cui stampo i risultati di akinformatica 
            schede_akinformatica = pp.akinformatica(scheda)
            nomi_akinformatica = schede_akinformatica["nome"]
            prezzi_akinformatica = schede_akinformatica["prezzo"]
            link_akinformatica = schede_akinformatica["link"]

            if not nomi_akinformatica:
                print("Non sono state trovate schede video su akinformatica \n")
            else:
                print("Schede trovate da akinformatica \n")
                for nome, prezzo, link in zip(nomi_akinformatica, prezzi_akinformatica, link_akinformatica):
                    print("Nome:", nome)
                    print("Prezzo:", prezzo)
                    print("Link prodotto:", link)
                    print("\n")
            print("--------------------------------------------------------------------------------------------")

            #parte in cui stampo i risultati di nexths
            schede_nexths = pp.nexths(scheda)
            nomi_nexths = schede_nexths["nome"]
            prezzi_nexths = schede_nexths["prezzo"]
            link_nexths = schede_nexths["link"]

            if not nomi_nexths:
                print("Non sono state trovate schede video su nexths \n")
            else:
                print("Schede trovate da nexths \n")
                for nome, prezzo, link in zip(nomi_nexths, prezzi_nexths,link_nexths):
                    print("Nome:", nome)
                    print("Prezzo:", prezzo)
                    print("Link prodotto:", link)
                    print("\n")
           
        elif scelta2 == 5:
            print("BAGLIONI MOVE!!")
            break

        else:
            raise ValueError()
    except ValueError:
        print("Devi inserire un numero intero valido")'''

