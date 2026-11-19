import pymongo


personnages = [
   { "name" : "Dagger", "ATK": 23, "DEF": 6, "PV": 105, "id" : 1},
   { "name" : "Blake", "ATK": 19, "DEF": 9, "PV": 95, "id" : 2},
   { "name" : "Ranger", "ATK": 17, "DEF": 15, "PV": 120,"id" : 3},
   { "name" : "Ace", "ATK": 25, "DEF": 3, "PV": 70, "id" : 4},
   { "name" : "Duke", "ATK": 14, "DEF": 12, "PV": 110, "id" : 5},
   { "name" : "Phoenix", "ATK": 22, "DEF": 8, "PV": 85,"id" : 6},
   { "name" : "Cobra", "ATK": 18, "DEF": 7, "PV": 90,"id" : 7},
   { "name" : "Hawk", "ATK": 20, "DEF": 5, "PV": 80, "id" : 8},
   { "name" : "Field", "ATK": 16, "DEF": 13, "PV": 90, "id" : 9},
   { "name" : "Striker", "ATK": 15, "DEF": 10, "PV": 100, "id" : 10}
]

monstres = [
   { "name" : "Nocthrax", "ATK": 25, "DEF": 15, "PV": 200, "id" : 1},
   { "name" : "Thirvaan", "ATK": 18, "DEF": 10, "PV": 100, "id" : 2},
   { "name" : "Bruthenkar", "ATK": 22, "DEF": 12, "PV": 150}, "id" : 3,
   { "name" : "Malavreth", "ATK": 28, "DEF": 18, "PV": 180, "id" : 4},
   { "name" : "Sylvakra", "ATK": 15, "DEF": 7, "PV": 90, "id" : 5},
   { "name" : "Ombrecorce", "ATK": 22, "DEF": 14, "PV": 140, "id" : 6},
   { "name" : "Croc-de-Givre", "ATK": 25, "DEF": 12, "PV": 130,"id" : 7},
   { "name" : "Silex", "ATK": 19, "DEF": 20, "PV": 170 , "id" : 8},
   { "name" : "Vesper", "ATK": 27, "DEF": 9, "PV": 105, "id" : 9},
   { "name" : "Écumeur", "ATK": 21, "DEF": 15, "PV": 155,"id" : 10}
]


# Création de la base de donnée et des collections
client = pymongo.MongoClient("mongodb://localhost:27017")
database = client["JEU_MONSTRE_B2"]

def init_db():
    collection_monstres = database["MONSTRES"]
    collection_personnages = database["PERSONNAGES"]
    collection_scores = database["SCORES"]

   #vide la base de données
    collection_personnages.drop()
    collection_monstres.drop()
    collection_scores.drop()


    #Insertion des données dans les différéntes collections
    collection_monstres.insert_many(monstres, bypass_document_validation = True)
    collection_personnages.insert_many(personnages, bypass_document_validation = True)

if __name__ == "__main__":
   init_db()
