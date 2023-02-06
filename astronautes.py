import requests

contenu = requests.get("http://api.open-notify.org/astros.json")
for personne in contenu.json()["people"]:
    for cle,valeur in personne.items():
        if cle == 'craft':
            if valeur == "ISS":
                print(personne)



