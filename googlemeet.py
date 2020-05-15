versione = 1.3

import webbrowser
import time
def actualversion(versione):
    actvers = open("actualversion.txt", "w")
    actvers.write(str(versione))
    actvers.close()

actualversion(versione)
#setting chrome come browser 
chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
webbrowser.register('miochrome', None,webbrowser.BackgroundBrowser(chrome_path))
a = webbrowser.get('miochrome')

#link e materie
italianolatino = "https://meet.google.com/ogr-kwwc-qhj"
matematicafisica = "https://meet.google.com/iuy-cgos-aks"
storiafilosofia = "http://meet.google.com/gcd-tqpz-pig"
scienze = "https://meet.google.com/epv-omdf-khn"
inglese = "https://meet.google.com/ret-owrh-vss"
arte = "https://meet.google.com/nke-tjis-cit"

giorno = time.strftime('%w')
ora = time.strftime("%H")


if giorno == '1': #lunedi
    if ora == "08":
        link = italianolatino
    elif ora == "09":
        link = italianolatino
    elif ora == "10":
        link = scienze
    elif ora == "12":
        link = storiafilosofia
    else:
        print("non c'è lezione")
    

elif giorno == '2': #martedi
    if ora == "08":
        link = storiafilosofia
    elif ora == "09":
        link = storiafilosofia
    elif ora == "10":
        link = inglese
    elif ora == "11":
        link = italianolatino
    else:
        print("non c'è lezione")
    
elif giorno == '3': #mercoledi
    if ora == "08":
        link = arte
    elif ora == "09":
        link = matematicafisica
    elif ora == "10":
        link = matematicafisica
    elif ora == "11":
        link = scienze
    elif ora == "12":
        link = inglese
    else:
        print("non c'è lezione")

elif giorno == '4': #giovedi
    if ora == "09":
        link = inglese
    elif ora == "10":
        link = matematicafisica
    elif ora == "11":
        link = matematicafisica
    elif ora == "12":
        link = arte
    else:
        print("non c'è lezione")

elif giorno == '5': #venerdi
    if ora == "08":
        link = italianolatino
    elif ora == "09":
        link = italianolatino
    elif ora == "10":
        link = storiafilosofia
    elif ora == "12":
        link = matematicafisica
    else:
        print("non c'è lezione")

elif giorno == '6': #sabato
    if ora == "08":
        link = italianolatino
    elif ora == "09":
        link = italianolatino
    elif ora == "10":
        link = matematicafisica
    elif ora == "11":
        link = matematicafisica
    else:
        print("non c'è lezione")

        

try: a.open(link)
except: 
    print("fra poco l'app si chiuderà")
    time.sleep(3)


