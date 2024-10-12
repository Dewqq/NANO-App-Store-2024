import sys
from Games import Nummer_Raad_Spel
from Games import Dagboek

def menu():
    while True:
        print("Welkom bij de NANO App Store!")
        print("1. Start Nummer Raad Spel")
        print("2. Start Dagboek")
        print("3. Verlaat")
        keuze = input("Kies een optie (1-3): ")

        if keuze == "1":
            Nummer_Raad_Spel.Nummer_Raad_Spel()  # Start het Nummer Raad Spel
        elif keuze == "2":
            Dagboek.dagboek()  # Start het Dagboek
        elif keuze == "3":
            print("Tot ziens!")
            sys.exit()  # Stop het programma
        else:
            print("Ongeldige invoer, probeer het opnieuw!")  # Ongeldige keuze
menu()