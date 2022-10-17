"""
Programme de calcul du prix d'un billet de transport journalier selon plusieurs rabais possibles.
    Prix normal d'un billet : 10chf
    Rabais étudiant : 2chf
    Rabais demi-tarif : 5chf
    Rabais groupe : 2 chf par billet acheté à partir de 4.
    Carte mensuelle : Billet gratuit

Indications :
    - Il est possible de bénéficier d'un rabais demi-tarif et étudiant
    - Le rabais groupe n’est cumulable avec aucun autre rabais
    - Il est possible d'avoir une carte mensuelle permettant d’avoir ce billet gratuitement

Contrainte : 
- Si la personne possède la carte mensuelle, il ne faut pas lui demander
d'autres informations.

"""
### Déclaration et initialisation des variables

carte_mensuelle_utlisateur: str = None
carte_demi_tarif_utilisateur: str = None
carte_etudiant_utilisateur: str = None
billets_voulus: int = None

prix_total = None
rabais_demi_tarif = None

carte_mensuelle_utlisateur: str = str(input("Possédez-vous la carte mensuelle ? (oui ou non)"))
carte_demi_tarif_utilisateur: str = str(input("Possédez-vous la carte demi tarif ? (oui ou non)"))
carte_etudiant_utilisateur: str = str(input("Possédez-vous la carte étudiant ? (oui ou non)"))

if(carte_mensuelle_utlisateur) == "oui":
    print("Le prix à payer est : 0 CHF")
if(carte_mensuelle_utlisateur == "non" and carte_demi_tarif_utilisateur == "non"):
    billets_voulus: int = int(input("Combien de billets voulez-vous ?"))



### Séquence d'opération

rabais_etudiant = str(input("Êtes-vous étudiant-e ? (oui ou non)"))
if rabais_etudiant == "oui":
    prix_total -= 2

rabais_groupe = str(input("Avez vous le tarif de groupe ) (oui ou non)"))
if rabais_groupe == "oui":
    prix_total -= 2
    if rabais_groupe == "oui" and rabais_demi_tarif == "oui":
        prix_total += 2
        if rabais_groupe == "oui" and rabais_etudiant == "oui":
            prix_total += 2
        if rabais_groupe == "oui":
        if rabais_groupe == "oui" and rabais_demi_tarif == "oui":
            prix_total += 2

carte_mensuelle_utlisateur = str(input("Avez-vous la carte mensuelle ? (oui ou non)"))
if carte_mensuelle_utlisateur == "oui":
    prix_total = 0

if prix_total >= 1:
    print("Le prix de votre billet est de ", prix_total,"CHF")
if carte_mensuelle_utlisateur == "oui":
