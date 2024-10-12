import random

def Nummer_Raad_Spel():
    getal = random.randint(1,100)

    print("Welkom bij het Nummer Raad Spel!")
    print("Ik heb een getal gekozen tussen de 1 en de 100")
    print("Je hebt 8 keer de kans om het juiste getal te raden!")
    print("Succes!")

    for beurt in range(1, 9):
        poging = int(input("Raad het getal: "))

        if poging > getal:
            print(f"Het getal is te hoog!")
        elif poging < getal:
            print(f"Het getal is te laag!")
        else:
            print("Gefeliciteerd! Je hebt het juiste getal gekozen!")
            break
    else:
        print(f"Jammer! Het juiste getal was: {getal} ")


