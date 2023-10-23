import os, time
from random import randrange

def obstacleBouge():
    obsta = 0
    obsAffAle = "♊🈸🈹"
    console_largeur = 150  # Vous pouvez ajuster cette valeur en fonction de la largeur de votre console
    position = randrange(console_largeur + len(obsAffAle))

    while obsta <= 7:
        obsta += 1
        pos = " " * position + obsAffAle
        print("" + "" * (console_largeur - 1) + "")
        print(pos)
        print("" + "" * (console_largeur - 1) + "")
        time.sleep(0.25)

        if obsta == 7:
            obsta = 0
            position = randrange(console_largeur +len(obsAffAle))
            os.system('cls' if os.name == 'nt' else 'clear')

obstacleBouge()
