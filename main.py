# Import
import pandas as pd
import requests  # Imports library for HTTP requests
from bs4 import BeautifulSoup as bs  # Imports BeautifulSoup for HTML parsing
import webbrowser # Imports a library to open pages on browsers
import os  # Imports library to interact with the operating system
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
cheapest_components={}
controllo = False
gpu_model = ""
cpu_infos={}
scelta = 0
budget = 0
preferenza = ""
cont,cheapest_cpu, cheapest_case, cheapest_dissipator, cheapest_gpu, cheapest_ssd, cheapest_pws, cheapest_motherBoard, cheapest_ram = 0, {}, {}, {}, {}, {}, {}, {}, {}

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
    exit()'''


    
# Request of the desired CPU
print("Request of the desired Intel CPU (processor)\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert: i5 14500\n")
    cpu_infos=cpu.cpu(input("insert the desired cpu:\n"))
    if cpu_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")
        
# Request of the desired MotherBoard
print("Request of the desired MoatherBoard\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert: B650 PLUS\n")
    mb_infos=mb.amazon_mother_boards(input("insert the desired MotherBoard:\n"))
    if cpu_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")
        
        
        
# Request of the desired Case
print("Request of the desired Corsair Case\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert: 4000D\n")
    case_infos=c.case(input("insert the desired case:\n"))
    if case_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")
        
# Request of the desired Arctic liquid freezer
print("Request of the desired Arctic liquid freezer\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert: 420\n")
    dissipator_infos=ld.dissipator(input("insert the desired liquid freezer model:\n"))
    if dissipator_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")
        
# Request of the desired NVIDIA GPU
print("Request of the desired NVIDIA GPU\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert: 4070 | 4070 super\n")
    gpu_infos=gpu.gpu(input("insert the desired GPU model:\n"))
    if gpu_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")
        
# Request of the desired SSD
print("Request of the desired SSD\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert: Samsung 1T\n")
    ssd_infos=ssd.ssd(input("insert the desired SSD model:\n"))
    if ssd_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")
        
# Request of the desired Power Supply
print("Request of the desired Corsair Power Supply\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert: 650W\n")
    pws_infos=pws.pws(input("insert the desired Pwoer Supply model:\n"))
    if ssd_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")
        
# Request of the desired Power Supply
print("Request of the desired Corsair Vengeance RAM\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert:16GB\n")
    ram_infos=ram.ram(input("insert the desired RAM model:\n"))
    if ssd_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")
        
print("What would you like to do now?") # asks what to do next
while True:
    try:
        scelta = int(input("Download the webpage of the cheapest products (1) | Show the cheapest products (2) | Open the pages on the browser (3) | Quit (4)\n")) # shows the options and waits for an answer
    except:
        print("insert a number")
    else:
        if 1<=scelta<=4: break
        else: print("Try again")

if scelta == 1: #searches the cheapest products and downloades the amazon webpage
    print("downloading CPU file")
    for i in zip(cpu_infos["price"], cpu_infos["link"]):
        if cont==0:
            cheapest_cpu["price"]=i[0]
            cheapest_cpu["link"]=i[1]
        else:
            if cheapest_cpu["price"]>i[0]: 
                cheapest_cpu["price"] = i[0]
                cheapest_cpu["link"]=i[1]
        cont+=1
    cont=0
    
    # Saving the file
    current_dir = os.path.dirname(__file__)
    cpu_file = f"cheapest_cpu.html"
    cpu_file_path = os.path.join(current_dir, cpu_file)
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'} # simulates a browser request
    response = requests.get(cheapest_cpu["link"], headers=HEADERS) # makes a HTTP request to the URL
    soup = bs(response.content, 'html.parser') # Analyzes the response
    # If the file exists deletes it
    if os.path.exists(cpu_file_path):
        os.remove(cpu_file_path)
    with open(cpu_file_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

    print("downloading CASE file")
    for i in zip(case_infos["price"], case_infos["link"]):
        if cont==0:
            cheapest_case["price"]=i[0]
            cheapest_case["link"]=i[1]
        else:
            if cheapest_case["price"]>i[0]: 
                cheapest_case["price"] = i[0]
                cheapest_case["link"]=i[1]
        cont+=1
    cont=0
    
    # Saving the file
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

    print("downloading LIQUID FREEZER file")
    for i in zip(dissipator_infos["price"], dissipator_infos["link"]):
        if cont==0:
            cheapest_dissipator["price"]=i[0]
            cheapest_dissipator["link"]=i[1]
        else:
            if cheapest_dissipator["price"]>i[0]: 
                cheapest_dissipator["price"] = i[0]
                cheapest_dissipator["link"]=i[1]
        cont+=1
    cont=0
    
    # Saving the file
    current_dir = os.path.dirname(__file__)
    dissipator_file = f"cheapest_dissipator.html"
    dissipator_file_path = os.path.join(current_dir, dissipator_file)
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'} # simulates a browser request
    response = requests.get(cheapest_dissipator["link"], headers=HEADERS) # makes a HTTP request to the URL
    soup = bs(response.content, 'html.parser') # Analyzes the response
    # If the file exists deletes it
    if os.path.exists(dissipator_file_path):
        os.remove(dissipator_file_path)
    with open(dissipator_file_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
    
    print("downloading MotherBoard file")
    for i in zip(mb_infos["price"], mb_infos["link"]):
        if cont==0:
            cheapest_motherBoard["price"]=i[0]
            cheapest_motherBoard["link"]=i[1]
        else:
            if cheapest_motherBoard["price"]>i[0]: 
                cheapest_motherBoard["price"] = i[0]
                cheapest_motherBoard["link"]=i[1]
        cont+=1
    cont=0
    
    # Saving the file
    current_dir = os.path.dirname(__file__)
    mb_file = f"cheapest_motherBoard.html"
    mb_file_path = os.path.join(current_dir, mb_file)
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'} # simulates a browser request
    response = requests.get(cheapest_motherBoard["link"], headers=HEADERS) # makes a HTTP request to the URL
    soup = bs(response.content, 'html.parser') # Analyzes the response
    # If the file exists deletes it
    if os.path.exists(mb_file_path):
        os.remove(mb_file_path)
    with open(mb_file_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
    
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
    cont=0
    
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

    print("downloading GPU file")
    for i in zip(gpu_infos["price"], gpu_infos["link"]):
        if cont==0:
            cheapest_gpu["price"]=i[0]
            cheapest_gpu["link"]=i[1]
        else:
            if cheapest_gpu["price"]>i[0]: 
                cheapest_gpu["price"] = i[0]
                cheapest_gpu["link"]=i[1]
        cont+=1
    cont=0
    
    # Saving the file
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
        .........CAMBIARE NOMI POWER SUPPLY
    print("downloading GPU file")
    for i in zip(gpu_infos["price"], gpu_infos["link"]):
        if cont==0:
            cheapest_gpu["price"]=i[0]
            cheapest_gpu["link"]=i[1]
        else:
            if cheapest_gpu["price"]>i[0]: 
                cheapest_gpu["price"] = i[0]
                cheapest_gpu["link"]=i[1]
        cont+=1
    cont=0
    
    # Saving the file
    current_dir = os.path.dirname(__file__)
    gpu_file = f"cheapest_powerSupply.html"
    gpu_file_path = os.path.join(current_dir, gpu_file)
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'} # simulates a browser request
    response = requests.get(cheapest_gpu["link"], headers=HEADERS) # makes a HTTP request to the URL
    soup = bs(response.content, 'html.parser') # Analyzes the response
    # If the file exists deletes it
    if os.path.exists(gpu_file_path):
        os.remove(gpu_file_path)
    with open(gpu_file_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
        
        ....... CAMBIARE RAM 
    print("downloading GPU file")
    for i in zip(gpu_infos["price"], gpu_infos["link"]):
        if cont==0:
            cheapest_gpu["price"]=i[0]
            cheapest_gpu["link"]=i[1]
        else:
            if cheapest_gpu["price"]>i[0]: 
                cheapest_gpu["price"] = i[0]
                cheapest_gpu["link"]=i[1]
        cont+=1
    cont=0
    
    # Saving the file
    current_dir = os.path.dirname(__file__)
    gpu_file = f"cheapest_ram.html"
    gpu_file_path = os.path.join(current_dir, gpu_file)
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'} # simulates a browser request
    response = requests.get(cheapest_gpu["link"], headers=HEADERS) # makes a HTTP request to the URL
    soup = bs(response.content, 'html.parser') # Analyzes the response
    # If the file exists deletes it
    if os.path.exists(gpu_file_path):
        os.remove(gpu_file_path)
    with open(gpu_file_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
        .........
        

elif scelta==2:
    print("searching cheaper CPU")
    for i in zip(cpu_infos["name"], cpu_infos["price"], cpu_infos["link"]):
        if cont==0:
            cheapest_cpu["title"]=i[0]
            cheapest_cpu["price"]=i[1]
            cheapest_cpu["link"]=i[2]
        else:
            if cheapest_cpu["price"]>i[1]: 
                cheapest_cpu["title"]=i[0]
                cheapest_cpu["price"]=i[1]
                cheapest_cpu["link"]=i[2]
        cont+=1
    cont=0
    print(f"I've found it\n")
    cheapest_components["cpu"]=cheapest_cpu
    
    print("searching cheaper CASE")
    for i in zip(case_infos["name"], case_infos["price"], case_infos["link"]):
        if cont==0:
            cheapest_case["title"]=i[0]
            cheapest_case["price"]=i[1]
            cheapest_case["link"]=i[2]
        else:
            if cheapest_case["price"]>i[1]: 
                cheapest_case["title"]=i[0]
                cheapest_case["price"]=i[1]
                cheapest_case["link"]=i[2]
        cont+=1
    cont=0
    print(f"I've found it\n")
    cheapest_components["case"]=cheapest_case
    
    print("searching cheaper LIQUID FREEZER")
    for i in zip(dissipator_infos["name"], dissipator_infos["price"], dissipator_infos["link"]):
        if cont==0:
            cheapest_dissipator["title"]=i[0]
            cheapest_dissipator["price"]=i[1]
            cheapest_dissipator["link"]=i[2]
        else:
            if cheapest_dissipator["price"]>i[1]: 
                cheapest_dissipator["title"]=i[0]
                cheapest_dissipator["price"]=i[1]
                cheapest_dissipator["link"]=i[2]
        cont+=1
    cont=0
    print(f"I've found it\n")
    cheapest_components["liquid_freezer"]=cheapest_dissipator
    
    print("searching cheapest GPU")
    for i in zip(gpu_infos["name"], gpu_infos["price"], gpu_infos["link"]):
        if cont==0:
            cheapest_gpu["title"]=i[0]
            cheapest_gpu["price"]=i[1]
            cheapest_gpu["link"]=i[2]
        else:
            if cheapest_gpu["price"]>i[1]: 
                cheapest_gpu["title"]=i[0]
                cheapest_gpu["price"]=i[1]
                cheapest_gpu["link"]=i[2]
        cont+=1
    cont=0
    print(f"I've found it\n{cheapest_gpu}")
    cheapest_components["gpu"]=cheapest_gpu
    
    

    print("searching cheapest SSD")
    for i in zip(ssd_infos["name"], ssd_infos["price"], ssd_infos["link"]):
        if cont==0:
            cheapest_ssd["title"]=i[0]
            cheapest_ssd["price"]=i[1]
            cheapest_ssd["link"]=i[2]
        else:
            if cheapest_ssd["price"]>i[1]: 
                cheapest_ssd["title"]=i[0]
                cheapest_ssd["price"]=i[1]
                cheapest_ssd["link"]=i[2]
        cont+=1
    cont=0
    print(f"I've found it\n")
    cheapest_components["liquid_freezer"]=cheapest_ssd
    
    #print(cheapest_components)
elif scelta==3:
    webbrowser.open(case_infos["link"])
    webbrowser.open(cpu_infos["link"])
    webbrowser.open(gpu_infos["link"])
    webbrowser.open(dissipator_infos["link"])
    webbrowser.open(mb_infos["link"])
    webbrowser.open(pws_infos["link"])
    webbrowser.open(ssd_infos["link"])
    webbrowser.open(ram_infos["link"])
else:
    print("We hope you had a nice time and you've found the perfect components for your PC. We hope to see you soon!")