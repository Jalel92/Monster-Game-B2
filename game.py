def demarrer_partie() :
    #demander le pseudo (appel la fonction correspondante)
    #création de l'équipe (appel de la fonction correspondante)
    #lancement de la bataille (appel de la fonction correspondante)
    #enregistre le score (appel de la fonction correspondante)

def en_vie() :
    #si l'entité a 0 pv :
        #retourne Vrai
    #sinon : 
        #retourn Faux 

def vague() :
    #creation d'une variable pour stocker le score de la vague
    #on tire au sort un monstre
    #le P1 attaque
    #le P2 attaque
    #le P3 attaque
    #le monstre attaque
    #si le monstre est mort (appel de la fonction en_vie):
        #ajout au score de la vague
        #on tire au sort un autre monstre
    #retourne le score

def bataille() :
    #creation d'une variable pour stocker le score final
    #tant que l'équipe est encore en vie : (appel de la fonction en_vie)
        #lancement d'une vague
        #stock le score de la vague
    #enregistre le score (appel de la fonction correspondante)


def enregistrer_score() :
    #enregistre le score dans mongo db