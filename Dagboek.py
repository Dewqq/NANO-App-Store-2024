from datetime import datetime
import csv
# import datetime voor de dag, maand en jaar
# import csv om te kunnen werken met CSV-bestanden

bestand = ("dagboek.csv")

def datum():
    while True: # Loop wordt gemaakt om de datum te vragen, voor het geval dat er een verkeerde invoer wordt ingevoerd
        inputdatum = input("Om welke dag gaat het? (vandaag / ander): ").strip() # overtollige spaties worden gestript
        if inputdatum == "vandaag":
            vandaag = datetime.today().strftime('%d-%m-%Y') # Huidige datum
            print("De datum van vandaag: " + vandaag)
            return vandaag
        elif inputdatum == "ander":
            datuminvoer = input("Voer de datum in die je wilt (Dag-Maand-Jaar): ").strip()
            try:
                # invoer wordt omgezet naar datum met specifieke formaat
                dagmaandjaar = datetime.strptime(datuminvoer, '%d-%m-%Y')
                print("Jouw ingevoerde datum = " + dagmaandjaar.strftime('%d-%m-%Y'))
                return dagmaandjaar.strftime('%d-%m-%Y')
            except ValueError:
                print("Je hebt een onjuiste datum gekozen! Probeer het opnieuw. ")
                # foutmelding verkeerde datuminvoer
        else:
            print("Je hebt een onjuiste datum gekozen! Probeer het opnieuw. ")
            # foutmelding ongeldige invoer

def datum_controle(datum):
    with open(bestand, 'r', newline='') as csvfile: # bestand wordt gelezen
        read = csv.reader(csvfile)
        for row in read:
            if datum in row: # er wordt gecontroleerd of de datum al in de rij staat
                print("Datum is al gebruikt.")
                return False # als datum al bestaat
    print("Datum is nog niet gebruikt.")
    return True # datum nog beschikbaar

def tekst_naar_dagboek(datum, tekst, herschrijven=False):
    if herschrijven:
        with open(bestand, 'r', newline='') as csvfile: # bestand wordt gelezen
            rows = list(csv.reader(csvfile)) # alle rijen worden in een lijst gelezen
        with open(bestand, 'w', newline='') as csvfile: # geopend om te kunnen schrijven
            writer = csv.writer(csvfile)
            for row in rows:
                if row[0] != datum: # als datum niet overeenkomt met de te herschrijven datum
                    writer.writerow(row) # schrijf de rij opnieuw in het bestand

    with open(bestand, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile) # CSV schrijver wordt aangemaakt
        writer.writerow([datum, tekst]) # datum & tekst wordt als een nieuwe rij geschreven
    print("Het dagboek is bijgewerkt voor datum: ", datum)

def dagboek():
    print("Welkom bij het dagboek!")
    gekozen_datum = datum()
    if datum_controle(gekozen_datum):
        tekstinput = input("Schrijf jouw tekst: ")
        tekst_naar_dagboek(gekozen_datum, tekstinput) # tekst & datum worden toegevoegd aan dagboke
    else:
        keuzeinput = input("Wil je de tekst herschrijven (h) of wil je tekst toevoegen (t)?: ")
        tekstinput = input("Schrijf jouw tekst: ")
        if keuzeinput == "h":
            tekst_naar_dagboek(gekozen_datum, tekstinput, herschrijven=True) # herschrijven van false naar true
        elif keuzeinput == 't':
            tekst_naar_dagboek(gekozen_datum, tekstinput)
        else:
            print("Ongeldige input! Probeer het opnieuw.") # foutmelding ongeldige keuze

