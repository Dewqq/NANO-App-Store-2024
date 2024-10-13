import random
# 'random' wordt geimporteerd om een willekeurige getal te kunnen kiezen

def Nummer_Raad_Spel():
    getal = random.randint(1,100)
    # Er wordt hier een willekeurige getal gekozen tussen de 1 en de 100

    print("Welkom bij het Nummer Raad Spel!")
    print("Ik heb een getal gekozen tussen de 1 en de 100")
    print("Je hebt 8 keer de kans om het juiste getal te raden!")
    print("Succes!")

    for beurt in range(1, 9): # 8 pogingen
        while True:
            try:
                poging = int(input("Raad het getal: "))
                break
            except ValueError: # Als er een ValueError optreedt dan krijgt de gebruiker een foutmelding
                print("Je mag alleen een getal invullen!")

        if poging > getal:
            print("Het getal is te hoog!")
        elif poging < getal:
            print("Het getal is te laag!")
        else: # Als de invoer en het getal hetzelfde is
            print("Gefeliciteerd! Je hebt het juiste getal gekozen!")
            break
    else: # De 8 beurten zijn voorbij
        print(f"Jammer! Het juiste getal was: {getal} ")



