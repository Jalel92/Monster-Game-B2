from db_init import *
from game import *

def choix_valide(choix_utilisateur, minimum_choix, maximum_choix) :
    # si le choix n'est pas isdigit()
        #retourner Faux
    # si le choix est entre minimum et maximum :
        #return True

def afficher_menu() :
    #afficher en tete
    #afficher consigne
    #afficher les choix (1.Demarrer une partie | 2. Afficher les 3 meilleurs scores | 3. Quitter le jeu) 
    #l'utilisateur rentre ses choix
    #tant que inifini
        #si la fonction choix_valide retourne faux
            #reproposer les choix en informant que le format précedent était mauvais
        #sinon
            #si le choix est 1 :
                #demarre la partie(appel de la fonctione correspondante)
            #si le choix est 2 :
                #affiche les 3 meilleurs scores(appel de la fonction correspondate)
            #si le choix est 3 :
                #quitte la partie (appel la fonction correspondante)


def creer_equipe():
    #afficher les personnages et leur competences (10 personnages numérotés pour une équipe de 3 maximum)
    #création d'une liste pour stocker les personnages de l'équipe
    # TANT que la longueur de la liste n'est pas égale 3
        #l'utilisateur rentre son choix
        #si le choix est entre 1 et 10 et qu'il n'est pas deja dans la liste de l'équipe
            #on l'ajoute a l'équipe
        #sinon : 
            #reproposer le choix
    # retourne la liste de l'équipe

def demander_pseudo() :
    #afficher la consigne
    #l'utilisateur rentre son pseudo (en string)
    #si le pseudo depasse 10 caractères :
        #reproposer le choix
    #retourne la chaine de caractères avec le pseudo

def quitter() :
    #quitte le jeu

def afficher_meilleurs_score() :
    #retourn les 3 meilleurs scores depuis mongodb

def main() :
    #affiche le menu
