"""
Programme simulant un distributeur de snacks
 Données : - Un montant entré par l'utilisateur
           - Un numéro d'article entré par l'utilisateur
 Indications :
           Le distributeur comporte :
           - Fanta orange à 2.90
           - Coca cola à 2.90
           - Coca cola light à 2.70
           - Henniez à 2.30
           - Ice Tea à 2.20
           - Limonade à 1.90
           
 Résultats : - Un message d’annulation de la transaction
                 (« Produit inconnu / Monnaie insuffisante »)
             - Un message indiquant la monnaie rendue si existante
             - Un message indiquant le produit vendu et souhaitant "santé"

"""

### Déclaration et initialisation des variables
argent_utilisateur: float = None
produit_selectionne: int = None

### Séquence d'opération

print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
print("1. Fanta Orange")
print("2. Coca cola")
print("3. Coca cola light")
print("4. Henniez")
print("5. Ice tea")
print("6. Limonade")
argent_utilisateur = (float)(input("Veuillez insérer votre monnaie : "))
produit_selectionne =(int)(input("Choisissez votre produit !:"))

#Fanta Orange
if(produit_selectionne==1):
    if(argent_utilisateur >= 2.9):
        print("voici votre Fanta orange")
        print("la machine vous rend :", argent_utilisateur-2.9)
        print("Votre Fanta Orange est servi. Santé !")
    else:
        print("Vous n'avez pas insérer assez de monnaie")

#Coca Cola
if(produit_selectionne==2):
    if(argent_utilisateur >= 2.9):
        print("voici votre Coca Cola")
        print("la machine vous rend :", argent_utilisateur-2.9)
        print("Votre Coca Cola est servi. Santé !")
    else:
        print("Vous n'avez pas insérer assez de monnaie")

#Coca Cola light
if(produit_selectionne==3):
    if(argent_utilisateur >= 2.7):
        print("voici votre Coca Cola light")
        print("la machine vous rend :", argent_utilisateur-2.7)
        print("Votre Coca Cola light est servi. Santé !")
    else:
        print("Vous n'avez pas insérer assez de monnaie")

#Henniez
if(produit_selectionne==4):
    if(argent_utilisateur >= 2.3):
        print("voici votre Henniez")
        print("la machine vous rend :", argent_utilisateur-2.3)
        print("Votre Henniez est servi. Santé !")
    else:
        print("Vous n'avez pas insérer assez de monnaie")

#Ice Tea
if(produit_selectionne==5):
    if(argent_utilisateur >= 2.2):
        print("voici votre Ice Tea")
        print("la machine vous rend :", argent_utilisateur-2.2)
        print("Votre Ice Tea est servi. Santé !")
    else:
        print("Vous n'avez pas insérer assez de monnaie")

#Limonade
if(produit_selectionne==6):
    if(argent_utilisateur >= 1.9):
        print("voici votre Limonade")
        print("la machine vous rend :", argent_utilisateur-1.9)
        print("Votre Limonade est servi. Santé !")
    else:
        print("Vous n'avez pas insérer assez de monnaie")



