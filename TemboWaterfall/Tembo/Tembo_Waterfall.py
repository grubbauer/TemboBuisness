#Not used code
#current_date = datetime.datetime.now()
#formatted_date = current_date.strftime("%d. %B %Y")
#Importing the librarys
import csv
import os
import random
import sys
import time
import pygame
#import datetime
import webbrowser
#Checking for init
pygame.init()
pygame.mixer.init()
#Startup sound
startup = pygame.mixer.Sound("startuptembo.wav")
startup.play()
#BASE VERSION
version = "1.1"
rightowner = "TERA CORPORATION"
businessholder = "TERA CORPORATION"
linum = 0  
if linum == 0:
    license = "TERA CORPORATION"
elif linum == 1:
    license = "Fully usable"
elif linum == 2:
    license = "Pirated copy"
    print("THIS IS A PIRATED COPY OF TEMBO WATERFALL")
    print("THIS WILL NOW BE SHUTDOWN AND WILL CHANGE")
    print("YOUR SYSTEM FILES ARE NOW COPYING AND WILL BE SENT TO THE OFFICIAL TERA SERVERS")

#loading the music files
try:
    pygame.mixer.music.load("91476_Glorious_morning.wav")
except FileNotFoundError as FNFE:
    print("Audio error:", FNFE)

# PRINTING USER INTERFACE
print("Tembo Waterfall")
print("Tera Business Managing App for Employees, Managing Team and Owner")
print("TBMAEMO")
print("Copyright (c)", rightowner)
print("Copyright (c)", businessholder)
print("Version", version)
print("License", license)
print("looking for details")
print("********************************")
print("All set")
#Null
Null = None
#Defining Variable as Null
basicmode = Null
admodebefore = Null
adminmodebefore = Null
adpass = Null
adminpassbefore = Null
admode = Null
ownerbool = Null
ownerboolinput = Null
adminmode = Null
music = Null
profilepath = Null
#Defining the command_2_en
def command_2_en():
    while True: 
        print("****************************************************************")
        print("append, menu, quit, make new profile, register new user profile")
        print("manage funds")
        command2 = input("What do you want to do now?: ")
        #Webtest(Not sure if working)
        if command2.lower() == "webtest":
            webbrowser.open("data:text/html,<html></html>")
        #Make new profile
        if command2.lower() == "make new profile":
            print("****************************************************************")
            b = 1
            pathb = str(b) + ".xml"
            while os.path.exists(pathb):
                b+=1
                pathb = str(b) + ".Xml"
            if not os.path.exists(pathb) and b != 0:
                print("Last MitarbeiterID:", (b - 1))
            elif b == 0:
                print("Last MitarbeiterID: No Profiles registered jet")
            newprofnum = input("Enter new profile number:")
            newprofpath = newprofnum + ".csv"
            if os.path.exists(newprofpath):
                print("New profile already exists")
            else:
                with open(newprofpath, 'w', newline='') as profwrite:
                    csv_writer = csv.writer(profwrite)
                    csv_writer.writerow(['Vorname', 'Nachname', 'MitarbeiterID', 'Beruf'])
                    VN = input("Vorname: ")
                    NN = input("Nachname: ")
                    MI = input("MitarbeiterID: ")
                    BR = input("Beruf: ")
                    csv_writer.writerow([VN, NN, MI, BR])
                    with open(pathb, 'w') as fileb:
                        fileb.write("Placeholder")
                        fileb.write("Placeholder")
        #managing the funds
        if command2.lower() == "manage funds":
            print("****************************************************************")
            a = 0
            filename_base = "geld.csv"
            fundbase = filename_base
            if os.path.exists(fundbase):
                with open(fundbase, 'r', newline='') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    for row in csv_reader:
                        print(', '.join(row))
            while os.path.exists(filename_base):
                os.remove(filename_base)
            
            if not os.path.exists(fundbase):
                with open(fundbase, 'w', newline='') as fundwrite:
                    csv_writer = csv.writer(fundwrite)
                    csv_writer.writerow(['Zahlungen', 'Aktien', 'Datum','Verkäufe','Gesamt'])
                    
                    P = input("Zahlungen: ")
                    S = input("Aktien: ")
                    D = input("Datum: ")
                    V = input("Verkäufe: ")
                    T = input("Gesamt: ")
                    csv_writer.writerow([P,S,D,V,T])
        #making new user profile
        if command2.lower() == "register new user profile":
            print("****************************************************************")
            a = 1
            patha = str(a) + ".json"
            while os.path.exists(patha):
                a+=1
                patha = str(a) + ".json"
            if not os.path.exists(patha) and a != 0:
                print("Last KundenID:", (a - 1))
            elif a == 0:
                print("Last Kunden ID: No Profiles registered jet")
            newuserpath = input("Enter new profile name:")
            newuserpath = newuserpath + ".csv"

            if os.path.exists(newuserpath):
                print("New profile already exists")    
            else:
                with open(newuserpath, 'w', newline='') as userwrite:
                    csv_writer = csv.writer(userwrite)
                    csv_writer.writerow(['Vorname', 'Nachname', 'KundenID', 'QRCODESECURITY'])
                    VN = input("Vorname: ")
                    NN = input("Nachname: ")
                    MI = input("KundenID: ")
                    QR = input("QRCODESECURITY: ")
                    csv_writer.writerow([VN, NN, MI,  QR])
                    with open(patha, 'w') as file:
                        file.write("Placeholder")
                        file.write("Placeholder")
        #appending a sale
        if command2.lower() == "append":
            print("****************************************************************")
            file_path = "Verkäufe.csv"  # Define the file path here
            new_row = []
            new_row.append(input("Vorname: "))
            new_row.append(input("Nachname: "))
            new_row.append(input("KundenNr.: "))
            new_row.append(input("BestellungsBezeichnung: "))
            new_row.append(input("Anrede: "))
            new_row.append(input("Stärke: "))
            new_row.append(input("Stärke2: "))
            new_row.append(input("ProduktNr: "))
            new_row.append(input("GanzerName: "))
            new_row.append(input("Einnahme: "))
            new_row.append(input("Datum: "))
            if  not os.path.exists(file_path):
                with open(file_path, 'w', newline='') as csvfile:
                                csv_writer = csv.writer(csvfile)
                                csv_writer.writerow(['Vorname', 'Nachname', 'KundenNr.', 'BestellungsBezeichnung', 'Anrede', 'Stärke', 'Stärke2', 'ProduktNr', 'GanzerName', 'Einnahme', 'Datum'])
            with open(file_path, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(new_row)
            print("New line appended to sales data.")
        #menu
        elif command2.lower() == "menu":
             break
        #quiting
        elif command2.lower() == "quit":
            print("Now quitting")
            sys.exit(0)
        #invalid inputs
        else:
            print("Invalid input.")
#defining command_2_de 
def command_2_de():
    while True: 
        print("****************************************************************")
        print("hinzufügen, menü, beenden, neues profil, neues kundenprofil")
        print("geld managen")
        command2 = input("Was willst du jetzt tun?: ")
        #make new profile
        if command2 == "neues profil":
            print("****************************************************************")
            b = 1
            pathb = str(b) + ".xml"
            while os.path.exists(pathb):
                b+=1
                pathb = str(b) + ".Xml"
            if not os.path.exists(pathb) and b != 0:
                print("Lezte MitarbeiterID:", (b - 1))
            elif b == 0:
                print("Lezte MitarbeiterID: Keine regestriert")
            newprofnum = input("Profile Nummer: ")
            newprofpath = newprofnum + ".csv"
            if os.path.exists(newprofpath):
                print("Profil exestiert bereits")      
            else:
                with open(newprofpath, 'w', newline='') as profwrite:
                    csv_writer = csv.writer(profwrite)
                    csv_writer.writerow(['Vorname', 'Nachname', 'MitarbeiterID', 'Beruf'])
                    VN = input("Vorname: ")
                    NN = input("Nachname: ")
                    MI = input("MitarbeiterID: ")
                    BR = input("Beruf: ")
                    csv_writer.writerow([VN, NN, MI, BR])
                    with open(pathb, 'w') as fileb:
                        fileb.write("Placeholder")
                        fileb.write("Placeholder")
        #managing funds
        if command2.lower() == "geld managen":
            print("****************************************************************")
            a = 0
            filename_base = "geld.csv"
            while os.path.exists(f"{a}{filename_base}"):
                a += 1
            fundbase = f"{a}{filename_base}"
            if not os.path.exists(f"{a}{fundbase}"):
                with open(fundbase, 'w', newline='') as fundwrite:
                    csv_writer = csv.writer(fundwrite)
                    csv_writer.writerow(['Zahlungen', 'Aktien', 'Datum','Verkäufe','Gesamt'])
                    
                    P = input("Zahlungen: ")
                    S = input("Aktien: ")
                    D = input("Datum: ")
                    V = input("Verkäufe: ")
                    T = input("Gesamt: ")
                    csv_writer.writerow([P,S,D,V,T])
        #make new user profile
        if command2.lower() == "neues kundenprofil":
            print("****************************************************************")
            a = 1
            patha = str(a) + ".json"
            while os.path.exists(patha):
                a+=1
                patha = a + ".json"
            if not os.path.exists(patha) and a != 0:
                print("Letzte KundenID:", (a - 1),"(Null = Nichts)")
            elif a == 0:
                print("Letzte KundenID:" + (a - 1))
            newuserpath = input("Neue Profilnummer:")
            newuserpath = newuserpath + ".csv"
            if os.path.exists(newuserpath):
                print("Neues Profil exestiert bereits")
            else:
                with open(newuserpath, 'w', newline='') as userwrite:
                    csv_writer = csv.writer(userwrite)
                    csv_writer.writerow(['Vorname', 'Nachname', 'KundenID', 'QRCODESECURITY'])
                    VN = input("Vorname: ")
                    NN = input("Nachname: ")
                    MI = input("KundenID: ")
                    QR = input("QRCODESECURITY")
                    csv_writer.writerow([VN, NN, MI,  QR])
                    with open(patha, 'w') as file:
                        file.write("Placeholder")
                        file.write("Placeholder")
        #Add sale
        if command2.lower() == "hinzufügen":
            print("****************************************************************")
            file_path = "Verkäufe.csv"  
            new_row = []
            new_row.append(input("Vorname: "))
            new_row.append(input("Nachname: "))
            new_row.append(input("KundenNr.: "))
            new_row.append(input("BestellungsBezeichnung: "))
            new_row.append(input("Anrede: "))
            new_row.append(input("Stärke: "))
            new_row.append(input("Stärke2: "))
            new_row.append(input("ProduktNr: "))
            new_row.append(input("GanzerName: "))
            new_row.append(input("Einnahme: "))
            new_row.append(input("Datum: "))
            if not os.path.exists(file_path):
                with open(file_path, 'w', newline='') as csvfile:
                                csv_writer = csv.writer(csvfile)
                                csv_writer.writerow(['Vorname', 'Nachname', 'KundenNr.', 'BestellungsBezeichnung', 'Anrede', 'Stärke', 'Stärke2', 'ProduktNr', 'GanzerName', 'Einnahme', 'Datum'])
            with open(file_path, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(new_row)
            print("Neuen Verkauf regestriert")
        #menu    
        elif command2.lower() == "menü":
            break  
        #quit
        elif command2.lower() == "beenden":
            print("Jetzt beenden")
            sys.exit(0)
        #invalid input
        else:
            print("Nicht gültig :(  ")
#Language input
language = input("EN=English, DE=Deutsch:")
if language == "English" or language == "EN":
    print("English is now selected")
    en = True
    de = False
elif language == "Deutsch" or language == "DE":
    print("Deutsch ist jetzt ausgewählt")
    de = True
    en = False
else:
    print("Error detected: language not specified: ", language)
    print("Fehler: sprache nicht definiert: ", language)
    sys.exit(1)
#if en is true
if en == True and de == False :
    #Music
    musicbool = input("Music(Yes|No): ")
    if musicbool == "Yes":
        music = True
    else:
        music = False
        print("****************************************************************")
    if music == True:
        #Copyright notice
        pygame.mixer.music.play(-1)
        print("****************************************************************")
        print("Music: Glorious Morning by Waterflame (CC BY 3.0)")
        print("Music Link: https://www.newgrounds.com/audio/listen/91476")
        print("License: https://creativecommons.org/licenses/by/3.0/")
        print("****************************************************************")
        print("Changes made:  made quieter")
    #Basic password
    basepas = input("Enter base password: ")
    if basepas == "w9$uHJcBzQ&3":
        baserunner = True
    else:
        print("FALSE")
        sys.exit(1)
#if de is true
elif de == True and en == False:
    #Music
    musicbool = input("Musik?(Ja|Nein)")
    if musicbool == "Ja":
        music = True
    else:
        music = False
        print("****************************************************************")
    if music == True:
        #Copyright Notice
        pygame.mixer.music.play(-1)
        print("****************************************************************")
        print("Musik: Glorious Morning by Waterflame (CC BY 3.0)")
        print("Musik Link: https://www.newgrounds.com/audio/listen/91476")
        print("Lizenz: https://creativecommons.org/licenses/by/3.0/")
        print("****************************************************************")
        print("Veränderungen: leiser gemacht")
    #Basic password
    basepas = input("Standart passwort eingeben: ")
    if basepas == "w9$uHJcBzQ&3":
        baserunner = True
    else:
        print("FALSCH")
        sys.exit(1)
#Anti Piracy 
if linum == 2:
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Privacy Detected.")
    time.sleep(0.1)
    pygame.display.set_caption("This is a crime.")
    time.sleep(0.1)
    pygame.display.set_caption("Privacy Detected.")
    time.sleep(0.1)
    pygame.display.set_caption("This is a crime.")
    time.sleep(0.1)
    pygame.display.set_caption("Privacy Detected.")
    time.sleep(0.1)
    pygame.display.set_caption("This is a crime.")
    time.sleep(0.1)
    a = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    if a == 1:
        background = pygame.image.load("aps2.png")
    else:
        background = pygame.image.load("aps.png")
    background = pygame.transform.scale(background, (800, 600))
    pygame.mixer.init()
    pygame.mixer.music.load("aps.wav")
    pygame.mixer.music.play(-1)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    time.sleep(13)

    file_to_delete = "base_library.zip"
    if os.path.exists(file_to_delete):
        os.remove(file_to_delete)
        print(f"{file_to_delete} deleted.")
    else:
        print(f"{file_to_delete} not found.")
    sys.exit(1)
#Baserunner
if baserunner and linum == 0 or 1:
    #English
    if en:
        print("****************************************************************")
        print("Right, you are now in the server")
        #Checking for job
        job = input("Enter your job, Basic(B),  Admin(Ad):")
        if job == "Basic" or job == "B":
            basicmode = True
        elif job == "Admin" or job == "ad" or job == "ADMIN" or "admin":
            adminmodebefore = True
    #German
    if de:
        print("****************************************************************")
        print("Richtig, du bist jetzt in dem Server")
        #Checking for job
        job = input("Was ist dein Job? Normal(B), , Admin(Ad): ")
        if job == "Normal" or job == "B":
            basicmode = True
        elif job == "Admin" or job == "ad" or job == "ADMIN" or "admin":
            adminmodebefore = True
#Notice if sucess
if basicmode:
    if en:
        print("Employee mode")
    if de:
        print("Mitarbeiter Modus")
#Checks admin passwords for german and english
if adminmodebefore :
    if en:
        adminpass = input("Admin Password: ")
        if adminpass == "Dn5#vRpMwX9":
            adminmode = True
    if de:
        adminpass = input("Admin Passwort: ")
        if adminpass == "Dn5#vRpMwX9":
            adminmode = True 
#Employee Mode
if basicmode:
    if en:
        #english
        while True:
            print("****************************************************************") 
            whatdo = input("What do you want to do?(send message to admins, view profile, register new sale, quit): ")
            #Message to admins
            if whatdo.lower() == "send message to admins":
                messageinput = input("What do you want to send to the admins? ")
                message = str(messageinput) + "\n"
                with open("newsales.json", 'a') as file:
                    file.write(message)
            if whatdo.lower() == "register new sale":
                VN = input("Vorname: ")
                NN = input("Nachname: ")
                BB = input("Bestellung: ")
                FB = input("Farbe")
                HKI = input("Hat Kunden Profil: ")
                WK = input("Will KundenID: ")
                DA = input("Datum: ")

                messageinput = (VN, NN, BB, FB, HKI, WK, DA)
                message = str(messageinput) + "\n"
                with open("newsales.json", 'a') as file:
                    file.write(message)
            #Viewing profile
            if whatdo.lower() == "view profile":
                print("****************************************************************")
                profileint = input("Enter profile Nr(Only Numbers): ")
                profilepath = profileint + ".csv" 
                if os.path.exists(profilepath):
                    with open(profilepath, 'r', newline='') as profilecsvfile:
                        csv_reader_prof = csv.reader(profilecsvfile)
                        for row in csv_reader_prof:
                            print(', '.join(row))
                else:
                    print("No profile found for", profilepath)
            #Quit
            if whatdo.lower() == "quit":
                sys.exit(0)
            
    if de:
        #german
        while True:
            print("****************************************************************")
            whatdo = input("Was willst du tun(sehe profil, nachricht zu den admins, neuer verkauf, beenden): ")
            print("****************************************************************")
            #message to admins
            if whatdo.lower() == "nachricht zu den admins":
                messageinput = input("Was willst du zu den admins schreiben: ")
                message = str(messageinput) + "\n"
                with open("message.json", 'a') as file:
                    file.write(message)
            if whatdo.lower() == "neuer verkauf":
                VN = input("Vorname: ")
                NN = input("Nachname: ")
                BB = input("Bestellung: ")
                FB = input("Farbe")
                HKI = input("Hat Kunden Profil: ")
                WK = input("Will KundenID: ")
                DA = input("Datum: ")

                messageinput = (VN, NN, BB, FB, HKI, WK, DA)
                message = str(messageinput) + "\n"
                with open("newsales.json", 'a') as file:
                    file.write(message)
            #view profile
            if whatdo.lower() == "sehe profil":
                profileint = input("profile Nr(Nummern): ")
                profilepath = profileint + ".csv" 
                if os.path.exists(profilepath):
                    with open(profilepath, 'r', newline='') as profilecsvfile:
                        csv_reader_prof = csv.reader(profilecsvfile)
                        for row in csv_reader_prof:
                            print(', '.join(row))
                else:
                    print("Kein Profil", profilepath)
            #quit
            if whatdo.lower() == "beenden":
                sys.exit(0)
#Admin mode
if adminmode:
    while True:
        #english
        if en:
            #Checking for owner or general admin
            print("****************************************************************")
            ownerboolinput = input("Are you an owner or general admin? Admin(A) Owner(O):")
            if ownerboolinput.lower() == "admin" or ownerboolinput.lower() == "a":
                adminmode = True
            elif ownerboolinput.lower() == "owner" or ownerboolinput.lower() == "o":
                ownerpass = input("Give me the owner password: ")
                if ownerpass == "Gc6%hKpNjZ4":
                    ownermode = True
                    print("Success")
                else:
                    print("NOOWNER")
            else:
                print("Invalid input.")
            if adminmode:
                while True:
                    print("****************************************************************")
                    print("continue, delete, view profile, see sales, quit, see messages, see new sales") 
                    command = input("Enter command: ")
                    #see messages
                    if command.lower() == "see new sales":
                        if os.path.exists("newsales.json"):
                            with open('newsales.json', 'r') as file:
                                content = file.read()
                                print("****************************************************************")
                                print("****************************************************************")
                                print(content)
                                print("****************************************************************")
                                print("****************************************************************")
                            os.remove("newsales.json")
                    if command.lower() == "see messages":
                        print("****************************************************************")
                        if os.path.exists("message.json"):
                            with open('message.json', 'r') as file:
                                content = file.read()
                                print(content)
                            os.remove("message.json") 
                        else:
                            print("****************************************************************") 
                            print("You have no new Messages!")
                            print("****************************************************************") 
                    #continue
                    elif command.lower() == "continue ":
                        print("****************************************************************")
                        placever = True
                        if placever == True:
                            print("Jumping to next commands")
                            command_2_en()
                    #deleting if owner
                    elif command.lower() == "delete":
                        print("****************************************************************")
                        if ownermode:
                            path = input("Enter file name, Raphi: ")
                            if os.path.exists(path):
                                os.remove(path)
                                print("Removed file")
                            elif not os.path.exists(path):
                                print("File does not exist")
                        elif ownermode == False:
                            print("Your not the owner")
                        command_2_en()
                    #viewing profiles
                    elif command.lower() == "view profile":
                        print("****************************************************************")
                        profileint = input("Enter profile Nr(For employees: MitarbeiterNr, Costumers: Name): ")
                        profilepath = profileint + ".csv" 
                        if os.path.exists(profilepath):
                            with open(profilepath, 'r', newline='') as profilecsvfile:
                                csv_reader_prof = csv.reader(profilecsvfile)
                                for row in csv_reader_prof:
                                    print(', '.join(row))
                        else:
                            print("No profile found for", profilepath)
                        command_2_en()
                    #see sales
                    elif command.lower() == "see sales":
                        print("****************************************************************")
                        file_path = 'Verkäufe.csv'
                        if os.path.exists(file_path):
                            with open(file_path, 'r', newline='') as csvfile:
                                csv_reader = csv.reader(csvfile)
                                for row in csv_reader:
                                    print(', '.join(row))
                        else:
                            with open(file_path, 'w', newline='') as csvfile:
                                csv_writer = csv.writer(csvfile)
                                csv_writer.writerow(['Vorname', 'Nachname', 'KundenNr.', 'BestellungsBezeichnung', 'Anrede', 'Stärke', 'Stärke2', 'ProduktNr', 'GanzerName', 'Einnahme', 'Datum'])
                        command_2_en()  
                    #quitting
                    elif command.lower() == "quit":
                        print("Now quitting")
                        sys.exit(0)
                    else:
                        print("Invalid input")
        #german
        elif de:
            #checking if normal or owner
            print("****************************************************************")
            ownerboolinput = input("Bist du der Besitzer oder ein genereller Administator?(Admin:a, Besitzer:o):")
            if ownerboolinput.lower() == "admin" or ownerboolinput.lower() == "a":
                adminmode = True
            elif ownerboolinput.lower() == "owner" or ownerboolinput.lower() == "o":
                ownerpass = input("Gib mir das Besitzer Passwort: ")
                if ownerpass == "Gc6%hKpNjZ4":
                    ownermode = True
                    print("Erfolg!")
                else:
                    print("KEINBESITER")
            else:
                print("Nicht gültige Eingabe")
            if adminmode:
                while True:
                    print("****************************************************************") 
                    print("weiter, löschen, sehe profil, verkäufe,sehe nachrichten, sehe neue verkäufe, beenden")
                    command = input("Befehl eingeben: ")
                    #see messages
                    if command.lower() == "sehe neue verkäufe":
                        if os.path.exists("newsales.json"):
                            with open('newsales.json', 'r') as file:
                                content = file.read()
                                print("****************************************************************")
                                print("****************************************************************")
                                print(content)
                                print("****************************************************************")
                                print("****************************************************************")
                            os.remove("newsales.json")
                    if command.lower() == "sehe nachrichten":
                        print("****************************************************************")
                        if os.path.exists("message.json"):
                            with open('message.json', 'r') as file:
                                content = file.read()
                                print(content)
                            os.remove("message.json")
                        else:
                            print("****************************************************************") 
                            print("Sie haben keine neuen Nachrichten!")
                            print("****************************************************************") 
                    #continue
                    elif command.lower() == "weiter ":
                        print("****************************************************************")
                        placever = True
                        if placever == True:
                            print("zu nächsten Befehleingabe springen")
                            command_2_de()    
                    #delete if owner
                    elif command.lower() == "löschen":
                        print("****************************************************************")
                        if ownermode:
                            path = input("Datei Name, Raphi: ")
                            if os.path.exists(path):
                                os.remove(path)
                            elif not os.path.exists(path):
                                print("Exestiert nicht")
                        elif ownermode == False:
                            print("KEINBESITZER")
                        command_2_de()
                    #see profile
                    elif command.lower() == "sehe profil":
                        print("****************************************************************")
                        profileint = input("ProfilNummer(Nummern für angestellte, Name für Kunden): ")
                        profilepath = profileint + ".csv" 
                        if os.path.exists(profilepath):
                            with open(profilepath, 'r', newline='') as profilecsvfile:
                                csv_reader_prof = csv.reader(profilecsvfile)
                                for row in csv_reader_prof:
                                    print(', '.join(row))
                        else:
                            print("Kein Profil", profilepath)
                        command_2_de()
                    #see sales
                    elif command.lower() == "verkäufe":
                        print("****************************************************************")
                        file_path = 'Verkäufe.csv'
                        if os.path.exists(file_path):
                            with open(file_path, 'r', newline='') as csvfile:
                                csv_reader = csv.reader(csvfile)
                                for row in csv_reader:
                                    print(', '.join(row))
                        else:
                            with open(file_path, 'w', newline='') as csvfile:
                                csv_writer = csv.writer(csvfile)
                                csv_writer.writerow(['Vorname', 'Nachname', 'KundenNr.', 'BestellungsBezeichnung', 'Anrede', 'Stärke', 'Stärke2', 'ProduktNr', 'GanzerName', 'Einnahme', 'Datum'])
                        command_2_de()        

                    elif command.lower() == "beenden":
                        print("Jetzt beenden")
                        sys.exit(0)
                    else:
                        print("Nicht gültig")