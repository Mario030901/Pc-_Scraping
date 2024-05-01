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
        
# Request of the desired Case
print("Request of the desired Corsair Case\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert: crystal 570X\n")
    case_infos=c.case(input("insert the desired case:\n"))
    if case_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")
        
# Request of the desired Arctic liquid freezer
print("Request of the desired Arctic liquid freezer\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert: 420\n")
    case_infos=ld.dissipator(input("insert the desired liquid freezer model:\n"))
    if case_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")
        
# Request of the desired NVIDIA GPU
print("Request of the desired NVIDIA GPU\n")
while True: #this while breaks when it finds a link, or better when the inserted model exists on amazon
    print("example of attended insert: 4070 | 4070 super\n")
    case_infos=gpu.gpu(input("insert the desired GPU model:\n"))
    if case_infos["link"]!=[]:
        break
    else: 
        print("the desired model doesn't exist on amazon, try searching something else\n")