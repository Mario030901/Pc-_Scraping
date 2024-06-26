# Import
import os   
import pandas as pd
import webbrowser # Imports a library to open pages on browsers
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
scelta = 0
budget = 0
preferenza = ""
case_model, cpu_model, gpu_model, lf_model, mb_model, pws_model, ssd_model = "", "", "", "", "", "", ""
cont,cheapest_cpu, cheapest_case, cheapest_dissipator, cheapest_gpu, cheapest_ssd, cheapest_pws, cheapest_motherBoard, cheapest_ram = 0, {}, {}, {}, {}, {}, {}, {}, {}
total_price=0



# Prima di procedere con la scelta della scheda, chiedi il budget e le preferenze dell'utente
try:
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

# Request of the desired Case
print("Request of the desired Corsair Case\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert: 4000D\n")
    case_model = input("insert the desired case:\n")
    case_infos=c.case(case_model)
    if case_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")
    
# Request of the desired CPU
print("Request of the desired Intel CPU (processor)\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert: i5 14500\n")
    cpu_model = input("insert the desired cpu:\n")
    cpu_infos=cpu.cpu(cpu_model)
    if cpu_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")
        
# Request of the desired NVIDIA GPU
print("Request of the desired NVIDIA GPU\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert: 4070 | 4070 super\n")
    gpu_model = input("insert the desired GPU model:\n")
    gpu_infos=gpu.gpu(gpu_model)
    if gpu_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")
        
# Request of the desired Arctic liquid freezer
print("Request of the desired Arctic liquid freezer\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert: 420\n")
    lf_model = input("insert the desired liquid freezer model:\n")
    dissipator_infos=ld.dissipator(lf_model)
    if dissipator_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")
        
# Request of the desired MotherBoard
print("Request of the desired MoatherBoard\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert: B650 PLUS\n")
    mb_model = input("insert the desired MotherBoard:\n")
    mb_infos=mb.amazon_mother_boards(mb_model)
    if mb_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")
        
# Request of the desired Power Supply
print("Request of the desired Corsair Power Supply\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert: 650W\n")
    pws_model = input("insert the desired Pwoer Supply model:\n")
    pws_infos=pws.pws(pws_model)
    if pws_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")
        
# Request of the desired RAM
print("Request of the desired Corsair Vengeance RAM and mhz\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert:16GB\n")
    ram_gb = input("insert the desired RAM model:\n")
    print("example of attended insert:3600\n")
    ram_hz = input("insert the desired RAM MHz:\n")
    ram_infos=ram.ram(ram_gb, ram_hz)
    if ram_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")
        
# Request of the desired SSD
print("Request of the desired SSD\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert: Samsung 1T\n")
    ssd_model = input("insert the desired SSD model:\n")
    ssd_infos=ssd.amazon_ssd(ssd_model)
    if ssd_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")
        
print("What would you like to do now?") # asks what to do next
while True:
    try:
        scelta = int(input("Download the webpage of the cheapest products (1) | Create an excel file with all the informations (2) | Open the pages on the browser (3) | Quit (4)\n")) # shows the options and waits for an answer
    except:
        print("insert a number")
    else:
        if 1<=scelta<=4: break
        else: print("Try again")
while scelta!=4:
    if scelta == 1: #searches the cheapest products and downloades the amazon webpage
        
        cheapest_case = c.find_cheapest(case_infos)
        c.download_file(cheapest_case)
        
        cheapest_cpu = cpu.find_cheapest(cpu_infos)
        cpu.download_file(cheapest_cpu)

        cheapest_gpu = gpu.find_cheapest(gpu_infos)
        gpu.download_file(cheapest_gpu)

        cheapest_dissipator = ld.find_cheapest(dissipator_infos)
        ld.download_file(cheapest_dissipator)
        
        cheapest_motherBoard = mb.find_cheapest(mb_infos)
        mb.download_file(cheapest_motherBoard)
        
        cheapest_pws = pws.find_cheapest(pws_infos)
        pws.download_file(cheapest_pws)
        
        cheapest_ram = ram.find_cheapest(ram_infos)
        ram.download_file(cheapest_ram)
        
        cheapest_ssd = ssd.find_cheapest(ssd_infos)
        ssd.download_file(cheapest_ssd)

    elif scelta==2:
        cheapest_case = c.find_cheapest(case_infos)
        cheapest_case["model"] = case_model
        cheapest_components["case"]=cheapest_case
        cheapest_case['price']=cheapest_case["price"].replace('.','')
        cheapest_case['price']=cheapest_case["price"].replace(',','.')
        total_price+= float(cheapest_case["price"][:-1])


        cheapest_cpu = cpu.find_cheapest(cpu_infos)
        cheapest_cpu["model"] = cpu_model
        cheapest_components["cpu"]=cheapest_cpu
        cheapest_cpu['price']=cheapest_cpu["price"].replace('.','')
        cheapest_cpu['price']=cheapest_cpu["price"].replace(',','.')
        total_price+= float(cheapest_cpu["price"][:-1])

        cheapest_gpu = gpu.find_cheapest(gpu_infos)
        cheapest_gpu["model"] = gpu_model
        cheapest_components["gpu"]=cheapest_gpu
        cheapest_gpu['price']=cheapest_gpu["price"].replace('.','')
        cheapest_gpu['price']=cheapest_gpu["price"].replace(',','.')
        total_price+= float(cheapest_gpu["price"][:-1])

        cheapest_dissipator = ld.find_cheapest(dissipator_infos)
        cheapest_dissipator["model"] = lf_model
        cheapest_components["liquid_freezer"]=cheapest_dissipator
        cheapest_dissipator['price']=cheapest_dissipator["price"].replace('.','')
        cheapest_dissipator['price']=cheapest_dissipator["price"].replace(',','.')
        total_price+= float(cheapest_dissipator["price"][:-1])

        cheapest_motherBoard = mb.find_cheapest(mb_infos)
        cheapest_motherBoard["model"] = mb_model
        cheapest_components["mother_board"]=cheapest_motherBoard
        cheapest_motherBoard['price']=cheapest_motherBoard["price"].replace('.','')
        cheapest_motherBoard['price']=cheapest_motherBoard["price"].replace(',','.')
        total_price+= float(cheapest_motherBoard["price"][:-1])

        cheapest_pws = pws.find_cheapest(pws_infos)
        cheapest_pws["model"] = pws_model
        cheapest_components["power_supply"]=cheapest_pws
        cheapest_pws['price']=cheapest_pws["price"].replace('.','')
        cheapest_pws['price']=cheapest_pws["price"].replace(',','.')
        total_price+= float(cheapest_pws["price"][:-1])

        cheapest_ram = ram.find_cheapest(ram_infos)
        cheapest_ram["gb"] = ram_gb
        cheapest_ram["hz"] = ram_hz
        cheapest_components["ram"]=cheapest_ram
        cheapest_ram['price']=cheapest_ram["price"].replace('.','')
        cheapest_ram['price']=cheapest_ram["price"].replace(',','.')
        total_price+= float(cheapest_ram["price"][:-1])

        cheapest_ssd = ssd.find_cheapest(ssd_infos)
        cheapest_ssd["model"] = ssd_model
        cheapest_components["ssd"]=cheapest_ssd
        cheapest_ssd['price']=cheapest_ssd["price"].replace('.','')
        cheapest_ssd['price']=cheapest_ssd["price"].replace(',','.')
        total_price+= float(cheapest_ssd["price"][:-1])

        build = pd.DataFrame(cheapest_components)
        if total_price>budget:
            comparison="budget exceeded"
        else:
            comparison="budget respected"
        total_price_df = pd.DataFrame({'Total Price': [total_price], 'Budget': [budget],'Comparison':[comparison]})
        current_dir = os.path.dirname(__file__)
        build_path = os.path.join(current_dir, 'build_pc.xlsx')
        budget_path = os.path.join(current_dir, 'budget.xlsx')
        build.to_excel('build_pc.xlsx', index=False)
        total_price_df.to_excel('budget.xlsx', index=False)

    elif scelta==3:
        cheapest_cpu=cpu.find_cheapest(cpu_infos)

        cheapest_gpu=gpu.find_cheapest(gpu_infos)

        cheapest_dissipator=ld.find_cheapest(dissipator_infos)

        cheapest_motherBoard=mb.find_cheapest(mb_infos)

        cheapest_pws=pws.find_cheapest(pws_infos)

        cheapest_ram=ram.find_cheapest(ram_infos)

        cheapest_ssd=ssd.find_cheapest(ssd_infos)
        
        cheapest_case=c.find_cheapest(case_infos)

        webbrowser.open(cheapest_case["link"])
        webbrowser.open(cheapest_cpu["link"])
        webbrowser.open(cheapest_gpu["link"])
        webbrowser.open(cheapest_dissipator["link"])
        webbrowser.open(cheapest_motherBoard["link"])
        webbrowser.open(cheapest_pws["link"])
        webbrowser.open(cheapest_ram["link"])
        webbrowser.open(cheapest_ssd["link"])
        
    elif scelta == 4:
        print("We hope you had a nice time and you've found the perfect components for your PC. We hope to see you soon!")
    else:
        print("choice not available, retry")
    
    print("What would you like to do now?") # asks what to do next
    scelta = int(input("Download the webpage of the cheapest products (1) | Create an excel file with all the informations (2) | Open the pages on the browser (3) | Quit (4)\n")) # shows the options and waits for an answer