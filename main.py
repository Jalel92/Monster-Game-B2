from db_init import *
from game import *
import os

def quitter() :
    os.system('cls' if os.name == 'nt' else 'clear')
    print("A bientôt !")

def afficher_meilleurs_score() :
    #retourn les 3 meilleurs scores depuis mongodb

def afficher_menu() :
    #afficher en tete
    print("Bienvenue dans le Jafar Monster Game !")
    #afficher consigne
    print("Séléctionner une des options suivantes pour continuer !")
    #afficher les choix (1.Demarrer une partie | 2. Afficher les 3 meilleurs scores | 3. Quitter le jeu)
    print("1. Démarrer une partie \n2. Afficher les 3 meilleurs scores\n3. Quitter le jeu") 
    #l'utilisateur rentre ses choix
    choix_utilisateur = input("Veuillez rentrer votre choix : ")
    #tant que inifini
    while True :
        #si la fonction choix_valide retourne faux
        if not choix_valide(choix_utilisateur,1,3) :
            #reproposer les choix en informant que le format précedent était mauvais
            choix_utilisateur = input("Veuillez rentrer un choix correct : ")
        #sinon
        else :
            #si le choix est 1 :
            if choix_utilisateur == 1: 
                #demarre la partie(appel de la fonctione correspondante)
                demarrer_partie()
            #si le choix est 2 :
            if choix_utilisateur == 2: 
                #affiche les 3 meilleurs scores(appel de la fonction correspondate)
                afficher_meilleurs_score()
            if choix_utilisateur == 3:                 
                #quitte la partie (appel la fonction correspondante)
                quitter()

def main() :
    pass
    #affiche le menu
