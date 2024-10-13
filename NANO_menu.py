import sys
from Games import Nummer_Raad_Spel
from Games import Dagboek
# sys-module wordt geimporteerd voor de systeemfunctionaliteiten
# De functies Nummer_Raad_Spel & Dagboek worden geimporteerd uit de 'Games' module

def menu():
    while True: # While-loop wordt gebruikt om steeds het menu te tonen totdat de gebruiker het systeem verlaat
        print("Welkom bij de Tiny App Showcase!")
        print("1. Start Nummer Raad Spel")
        print("2. Start Dagboek")
        print("3. Verlaat")
        keuze = input("Kies een optie (1-3): ")

        if keuze == "1":
            Nummer_Raad_Spel.Nummer_Raad_Spel()
        elif keuze == "2":
            Dagboek.dagboek()
        elif keuze == "3":
            print("Tot ziens!")
            sys.exit()
        else:
            print("Ongeldige invoer, probeer het opnieuw!")  # Ongeldige keuze, opnieuw proberen
menu() # De functie oproepen

