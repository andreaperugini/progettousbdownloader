import requests
import os
import sys
import shutil

n = "USBTOOL.py"
uvers = "https://github.com/andreaperugini/progettousbdownloader/raw/master/versione.txt"
uapp = "https://github.com/andreaperugini/progettousbdownloader/raw/master/USBTOOL.py"

def updating(nomeprogramma, urlvers, urlapp):
    
    r = requests.get(urlvers)
    fileversione = "versionegit.txt"
    file = open(fileversione, "wb") 
    file.write(r.content)
    file.close()
    try:
        versioneattuale = open("actualversion.txt", "r").readline(4)
        versioneaggiornamento = open("versionegit.txt", "r").readline(4)
        print("versione attuale: "+versioneattuale)
        print("versiona aggiornata: "+versioneaggiornamento)

        if float(versioneaggiornamento) > float(versioneattuale):
            print("c'è un aggiornamento")
            print("scarico aggiornamento")
            download = requests.get(urlapp)
            nuovoscript = open(nomeprogramma, "wb") 
            nuovoscript.write(download.content)
            nuovoscript.close()
            #os.system("python googlemeet.py")#sys.exit()
        else:
            print("nessun aggiornamento")
            pass

    except:
        print("file versione attuale non trovato")

updating(n, uvers, uapp)
os.system("python C:\\TemP\\nope\\"+n)




    

