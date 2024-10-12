from datetime import datetime
import csv

bestand = ("dagboek.csv")

def datum():
    while True:
        inputdatum = input("Om welke dag gaat het? (vandaag / ander): ").strip().lower()
        if inputdatum == "vandaag":
            vandaag = datetime.today().strftime('%d-%m-%Y')
            print("De datum van vandaag: " + vandaag)
            return vandaag
        elif inputdatum == "ander":
            datuminvoer = input("Voer de datum in die je wilt (Dag-Maand-Jaar): ").strip().lower()
            try:
                dagmaandjaar = datetime.strptime(datuminvoer, '%d-%m-%Y')
                print("Jouw ingevoerde datum = " + dagmaandjaar.strftime('%d-%m-%Y'))
                return dagmaandjaar.strftime('%d-%m-%Y')
            except ValueError:
                print("Je hebt een onjuiste datum gekozen! Probeer het opnieuw. ")
        else:
            print("Je hebt een onjuiste datum gekozen! Probeer het opnieuw. ")

def datum_controle(datum):
    with open(bestand, 'r', newline='') as csvfile:
        read = csv.reader(csvfile)
        for row in read:
            if datum in row:
                print("Datum is al gebruikt.")
                return False
    print("Datum is nog niet gebruikt.")
    return True

def tekst_naar_dagboek(datum, tekst, herschrijven=False):
    if herschrijven:
        with open(bestand, 'r', newline='') as csvfile:
            rows = list(csv.reader(csvfile))
        with open(bestand, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in rows:
                if row[0] != datum:
                    writer.writerow(row)

    with open(bestand, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([datum, tekst])
    print("Het dagboek is bijgewerkt voor datum: ", datum)

def dagboek():
    print("Welkom bij het dagboek!")
    gekozen_datum = datum()
    if datum_controle(gekozen_datum):
        tekstinput = input("Schrijf jouw tekst: ")
        tekst_naar_dagboek(gekozen_datum, tekstinput)
    else:
        keuzeinput = input("Wil je de tekst herschrijven (h) of wil je tekst toevoegen (t)?: ")
        tekstinput = input("Schrijf jouw tekst: ")
        if keuzeinput == "h":
            tekst_naar_dagboek(gekozen_datum, tekstinput, herschrijven=True)
        elif keuzeinput == 't':
            tekst_naar_dagboek(gekozen_datum, tekstinput)
        else:
            print("Ongeldige input! Probeer het opnieuw.")

