"""
Programme testant si une date, saisie par l'utilisateur, est valide ou non.
Données : Une date saisie par l'utilisateur
Indications:
        Pour pouvoir déterminer si une année est bissextile :       
        	- Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
        	- Si elle est multiple de 4, on regarde si elle est multiple de 100.
            	- Si c'est le cas, on regarde si elle est multiple de 400.
      		- Si c'est le cas, l'année est bissextile.
                        		- Sinon, elle n'est pas bissextile.
- Sinon, elle est bissextile.

Résultats : Un message spécifiant si la date entrée est valide.

"""

### Déclaration et initialisation des variables

jour: int = int(input("Saississez un jour :"))

mois: int = int(input("Saississez un mois :"))

annee: int = int(input("Saisissez une année :"))

bissextile: bool = False

if (annee % 4) != 0:
    bissextile = False
if (annee % 4 == 0) and (annee % 100) == 0:
    bissextile = True
if (annee % 4 == 0) and (annee % 100) == 0:
    if (annee % 400) == 0:
        bissextile = True



if (mois > 12 or mois < 1) or (jour > 31 or jour < 1):
    print("Cette date n'est pas valide")
elif(mois < 12 or mois < 1) or (jour < 31 or jour < 1):
    if(mois == 4 or mois == 6 or mois == 9 or mois == 11):
        if(jour <=30):
            print("Cette date est valide.")
        else:print("Cette date n'est pas valide.")
    elif(mois == 2):
        if(not bissextile):
            print("Cette date est valide.")
        elif(jour > 28):
            print("Cette date n'est pas valide.")
    elif(bissextile):
        if(jour <= 29):
            print("Cette date est valide.")
        elif(jour > 29):
            print("Cette date n'est pas valide.")

    elif(mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12):
        if(jour <= 31):
            print("Cette date est valide.")

    elif (mois == 2) and (bissextile) and (jour <= 29):
        print("Cette date est valide")
    elif (mois == 2) and (not bissextile) and (jour <= 28):
        print("Cette date est valide")
    else:
        print("Cette date n'est pas valide.")








### Séquence d'opération


        
