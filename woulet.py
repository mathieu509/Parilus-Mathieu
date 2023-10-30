from random import randrange
import pickle
import os 

nbr  = randrange(0,1,2) 

try:
    with open('scores.pkl', 'rb') as fichier_scores:
        scores = pickle.load(fichier_scores)
except FileNotFoundError:
    scores = {}

def pran_epsedo():
    while True:
        print("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")

        pseudo = input("Entre epsedo , NB:li sipoze an miniskil e san espas : ")
        if ' ' in pseudo:
           pseudo=input("pa sipoze gen espas re antre epsedo a")
        if not pseudo.islower():
           pseudo=input("epsedo a dwe an miniskil")  
        print("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")

        
        return pseudo


def jouer_roulette():
    print("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")
    print("Byenvini nan Jwet woulet la👍👍👍👍👍!")
    print("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")
    print("gen yn nomb ke jwet la chwazi nan enteval 1 a 10000")
    print("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")

    
pseudo = pran_epsedo()

nonb_ese = 0
nb_chans = 5
kanpe=False
while True:
    while nb_chans > 0:
            nonb_ese += 1
            try:
                nb_devine = int(input(f"Ese {nonb_ese}:entre yn nonb : "))
                if nb_devine == nbr:
                    print("BRAVO!🧑🏽👨🏽👨🏽👩🏽👩🏽 ou genyen!")
                    print(f"nonb kache se: {nbr}")
                    score = nb_chans * 10
                    if pseudo in scores:
                        scores[pseudo] += score
                    else:
                        scores[pseudo] = score
                    with open('scores.pkl', 'wb') as fichier_scores:
                        pickle.dump(scores, fichier_scores)
                    print(f"esko ou pou pati sa se: {score}")
                    print(f"esko total la se:{pseudo} {scores[pseudo]}")
                   
                    break
                elif nb_devine < 1 or nb_devine > 10000:
                    print("nonb ou antre a pa nan enteval la.")
                elif nb_devine < nbr:
                    print("nonb kache a pi gwo😋.")
                else:
                    print("nonb kache a pi piti😎.")
                nb_chans -= 1
                print(f"ou rete  : {nb_chans}  chans")
            except ValueError:
                print("Entre yn nonb ki valid.")
        
            if nb_chans == 0:
             print(f"sorry ou itilize tout chans ou t genyen yo. nonb kache a c: {nbr}")

    

    jouer_roulette()
    kanpe = input("tape 'K' pou kanpe jwet la)").strip().lower()
    if kanpe == 'k':
            break
    





