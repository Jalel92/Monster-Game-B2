from  pymongo import MongoClient
import random

def choix_valide(choix_utilisateur, minimum_choix, maximum_choix) :
    if choix_utilisateur.isdigit() :
        return False
    if not choix_utilisateur >= minimum_choix and choix_utilisateur <= maximum_choix :
        return False
    return True

def team_fusion(team,liste_personnages) :
    final_team = []
    for e in team :
        for i in range(len(liste_personnages)) :
             if e == liste_personnages[i]["id"] :
                 final_team.append(liste_personnages[i])
    return final_team

def recuperer_personnages_db():
    client = MongoClient("mongodb://localhost:27017")
    db = client["JEU_MONSTRE_B2"]
    curseur = db["PERSONNAGES"].find()
    liste_personnages = list(curseur)
    return liste_personnages

def creer_equipe(perso_db):
    print("Compose ton équipe de 3 personnages :" )
    #afficher les personnages et leur competences (10 personnages numérotés pour une équipe de 3 maximum)
    #création d'une liste pour stocker les personnages de l'équipe
    team = []
    # TANT que la longueur de la liste n'est pas égale 3
    while len(team) != 3 :
        #l'utilisateur rentre son choix
        choix_utilisateur = input("Rentrez l'id du personnage souhaitée")
        #si le choix est entre 1 et 10 et qu'il n'est pas deja dans la liste de l'équipe
        for i in range(len(team)) :
            if team[i] == choix_utilisateur :
                choix_utilisateur = input("Rentrez l'id d'un personnage non présent dans l'équipe !")
            else :
                 if choix_valide(choix_utilisateur,1,10) :
                    team.append(choix_utilisateur)
    # retourne la liste de l'équipe
    team = team_fusion(team, perso_db) #au lieu d'avoir un liste avec juste des numeros, on revoie la vrai équipe avec les vrais persos (leurs pv, atk etc tirés directement depuis db_init)
    return team

def demander_pseudo() :
    #l'utilisateur rentre son pseudo
    pseudo_utilisateur = input("Veuillez rentrer votre pseudo : ")
    #si le pseudo depasse 10 caractères :
    if len(pseudo_utilisateur) > 10 or len(pseudo_utilisateur) < 1 :
        pseudo_utilisateur = input("Veuillez rentrer un pseudo correct : ")
    return pseudo_utilisateur()



def recuperer_monstre_db():
    client = MongoClient("mongodb://localhost:27017")
    db = client["JEU_MONSTRE_B2"]
    curseur = db["MONSTRES"].find()
    liste_monstre = list(curseur)
    return liste_monstre


def demarrer_partie() :
    pseudo = demander_pseudo()
    persos = recuperer_personnages_db()
    team = creer_equipe(persos)
    monstres = recuperer_monstre_db()
    score_game = bataille(team,monstres)
    enregistrer_score(pseudo, score_game)

def en_vie(entite) :
    if entite["PV"] > 0 :
        return True
    else :
        return False

def choix_monstre(monstres) :
    monstres_en_vie = recuperer_monstre_en_vie(monstres)
    monstre = random.choice(monstres_en_vie)
    return monstre

def recuperer_monstre_en_vie(monstres):
    monstres_vie = []
    for i in range(len(monstres)) :
        if monstres[i]["PV"] > 0 :
            monstres_vie.append(monstres[i])
    return monstres_vie

def personnages_equipe_en_vie(team):
    personnages_vie = []
    for i in range(len(team)) :
        if team[i]["PV"] > 0 :
            personnages_vie.append(team[i])
    return personnages_vie

def monstre_attack(team, monstre) : 
    team[0]["PV"]  = team[0]["PV"] - monstre["ATK"]
    team[1]["PV"]  = team[1]["PV"] - monstre["ATK"]
    team[2]["PV"]  = team[2]["PV"] - monstre["ATK"]


def team_attack(team, monstre) :

    if en_vie(team[0]) :
        monstre["PV"] = monstre["PV"] - team[0]["ATK"]
    if en_vie(team[1]) :
        monstre["PV"] = monstre["PV"] - team[1]["ATK"]
    if en_vie(team[2]) :
        monstre["PV"] = monstre["PV"] - team[3]["ATK"]
    return monstre["PV"]

def vague(team,monstres) :
    #creation d'une variable pour stocker le score de la vague
    score_vague = 0
    team = team
    #on tire au sort un monstre
    monstre = choix_monstre(monstres)
    #l'équipe attaque
    team_attack(team,monstre)
    #le monstre attaque
    monstre_attack(team,monstre)
    #si le monstre est mort (appel de la fonction en_vie):
    if not en_vie(monstre) :
        #ajout au score de la vague
        score_vague += 1
    #retourne le score
    return score_vague

def en_vie_equipe(team) :
    len_team = len(team)
    L2 = []
    for e in team :
        if e["PV"] <= 0 :
            L2.append(e)
    if len(L2) == len_team :
        return True
    return False

def bataille(equipe, monstres) :
    #creation d'une variable pour stocker le score final
    score_final = 0
    #tant que l'équipe est encore en vie : (appel de la fonction en_vie)
    while en_vie_equipe(equipe) :
        #lancement d'une vague
        score_final += vague(equipe,monstres)
    return score_final


def enregistrer_score() :
    #enregistre le score dans mongo db