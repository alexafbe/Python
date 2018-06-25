#A.Fabre
import random

values = {7, 8, 9, 10, "Valet", "Dame", "Roi", "As"}
colors = {"pique", "carreau", "trefle", "coeur"}

#Création du paquet
def Cards() :
    return [(x,y) for x in values for y in colors]
Game = Cards()

#Mélange des cartes
random.shuffle(Game)

#Pioche
pioche = random.choice(Game)
print(pioche)

#Jeu, victoire / défaite
if pioche[0] == 'Roi' :
    print("Bravo, vous avez gagné !")
else :
    print("Pas Bravo, vous avez perdu")
