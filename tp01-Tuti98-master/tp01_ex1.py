"""
Programme permettant de convertir une quantité en plusieurs unités d'énergie.

1J  =  0.738 ft-lb  =  0.239 cal  =  6.24*10^18 eV

Unités : joule, calorie, Ft-lb et eV
  Données : Une valeur et une unité
  Indications:
        Selon l'unité entrée par l'utilisateur, afficher la conversion
        dans les 3 autres unités.
  Résultats : Affichage des conversions
"""

### Déclaration et initialisation des variable

quantite: int = float(input("Quel est votre quantite d'energie ?"))
unite: str = input("Quel est votre unite ?")

print("valeur en entrée :" + str(quantite) + " "+ unite)


### Séquence d'opération

if unite == "j":
    quantite1 = (quantite * 0.738)
    quantite2 =(quantite * 0.239)
    quantite3 = (quantite*6.24*10**18)
    print(("en ft-lb :"), quantite1,"ft-lb")
    print(("en calories :"), quantite2, "cal")
    print(("en eV"),quantite3, "eV")

elif unite == "ft-lb":
    quantite4 = (quantite / 0.738)
    quantite5 = (quantite * 0.239 / 0.738)
    quantite6 = (quantite * 6.24*10**18 / 0.738)
    print(("en joule"),quantite4, "j")
    print(("en calories"), quantite5, "cal")
    print(("en eV"), quantite6, "eV")

elif unite == "cal":
    quantite7 = (quantite / 0.239)
    quantite8 = (quantite * 0.738 / 0.239)
    quantite9 = (quantite *6.24*10**18 / 0.239)
    print(("en joule"),quantite7, "j")
    print(("en ft-lb"), quantite8,"ft-lb")
    print(("en eV"),quantite9,"eV")

elif unite == "eV":
    quantite10 = (quantite / 6.24*10**18)#cal
    quantite11 = (quantite *0.738 / 6.24*10**18 )#
    quantite12 = (quantite * 0.239 / 6.24*10**18)
    print(("en joule"), quantite10, "j")
    print(("en ft-lb"), quantite11, "ft-lb")
    print(("en calories"), quantite12, "cal")
