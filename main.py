from db_init import *

def afficher_menu() :
    #afficher en tete
    #afficher consigne
    #afficher les choix (1.Demarrer une partie | 2. Afficher les 3 meilleurs scores | 3. Quitter la partie) 
    #l'utilisateur rentre ses choix
    #si le choix n'est pas dans 1,2 ou 3
        #reproposer les choix en informant que le format précedent était mauvais
    #sinon
        #si le choix est 1 :
            #demarre la partie(appel de la fonctione correspondante)
        #si le choix est 2 :
            #affiche les 3 meilleurs scores(appel de la fonction correspondate)
        #si le choix est 3 :
            #quitte la partie


def creer_equipe():
    #afficher les personnages et leur competences (10 personnages numérotés pour une équipe de 3 maximum)
    #création d'une liste pour stocker les personnages de l'équipe
    # TANT que la longueur de la liste n'est pas égale 3
        #l'utilisateur rentre son choix
        #si le choix est entre 1 et 10 et qu'il n'est pas deja dans la liste de l'équipe
            #on l'ajoute a l'équipe
        #sinon
            #reproposer le choix
    # retourne la liste de l'équipe

def demander_pseudo() :
    #afficher la consigne
    #l'utilisateur rentre son pseudo (en string)
    #si le pseudo depasse 10 caractères :
        #reproposer le choix
    #retourn la chaine de caractères avec le pseudo

def enregistrer_score() :
    pass

def nouvelle_partie() :
    pass

def afficher_meilleurs_score() :
    pass

def main() :
    pass