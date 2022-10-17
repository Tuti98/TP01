"""
Programme calculant le niveau de risque cardiovasculaire. 
  Données : - L'Age de l'utilisateur
            - Le sexe de l'utilisateur
            - Si l'utilisateur est un fumeur ou non
            - Si l'utilisateur pratique du sport
            - Si l’utilisateur possède une alimentation trop sucrée
  Indications :
            - Si l'utilisateur est fumeur, le niveau de risque augmente de 2
            - Si l'utilisateur fait du sport, le niveau de risque diminue de 1
            - Si l'utilisateur est un homme de plus de 50 ans,
              le niveau de risque augmente de 1
            - Si l'utilisateur est une femme de plus de 60ans,
              le niveau de risque augmente de 1
            - Si l’utilisateur consomme trop de sucre, le niveau de risque augmente de 2
            
  Résultats : Un message spécifiant le niveau de risque obtenu.
            - Si le niveau de risque est inférieur ou égal à 1, le niveau de risque est faible.
            - Si le niveau de risque est de 2 à 3, le niveau de risque est élevé
            - Sinon il est très élevé.

"""
### Déclaration et initialisation des variables
user_age: int = int(input("Quel est votre âge ?"))
user_sexe: str = input("Quel est votre sexe ? (H ou F)")
is_smoker: str = input("Êtes-vous fumeur ? (oui ou non)")
user_sport: str = input("Pratiquez-vous du sport ? (oui ou non)")
sugar_consumption: str = input("Avez-vous une alimentation qui comporte beaucoup de sucres ? (oui ou non)")

risk_factor: int = 0



### Séquence d'opération

if is_smoker == "oui": risk_factor += 2

if user_sport == "oui": risk_factor -= 1

if user_sexe == "H" and user_age >= 50: risk_factor += 1

if user_sexe == "F" and user_age >= 60: risk_factor += 1

if sugar_consumption == "oui": risk_factor += 2

if risk_factor <= 1:
    print("Le niveau de risque est faible")


elif risk_factor == 2 or risk_factor == 3:
    print("Le niveau de risque est élevé")

elif risk_factor > 3:
    print("Le niveau de risque est très élévé")






