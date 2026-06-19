import json

def menu() :
    print("=== Gestion Budget ===\n1. Ajouter un revenu\n2.Ajouter une dépense\n3.Voir le résumé\n4.Voir les détails\n5.Quitter")

    pm = False
    while not pm :
        select = input("Choisir un choix !")
        if not select.isdigit() :
            print("Invalid Input")
            continue

        select = int(select)

        if not (1<=select<=5) :
            print("Invalid Input")
            continue
        else :
            return select

def sauvegarder(revenus, depenses):
    data = {
        "revenus": revenus,
        "depenses": depenses
    }

    with open("budget.json", "w") as f:
        json.dump(data, f, indent=4)


def charger():
    try:
        with open("budget.json", "r") as f:
            data = json.load(f)
            return data["revenus"], data["depenses"]

    except FileNotFoundError:
        revenus = [1500, 200]
        depenses = {
            "food": [20, 15, 40],
            "transport": [30, 10],
            "sport": [50]
        }
        return revenus, depenses


def afficher_résumé(total_revenu, total_depenses,total_economie,catégorie) :
     fichier = open("résumé.txt","a")
     fichier.write(f"=== Résumé Budget ===\nTotal revenus : {total_revenu}\nTotal dépenses : {total_depenses}\nEconomies : {total_economie}\nCatégorie la plus chère : {catégorie}  ")

def ajout(select,revenus,depenses) :

    if select == 1 :
        pm = False
        while not pm:
            select = input("Tu as choisi l'option(Ajouter un revenu) !\nChoisir un montant !")
            if not select.isdigit():
                print("Invalid Input")
                continue
            select = int(select)

            if select < 0 :
                print("Invalid Input")
                continue
            else :
                revenus.append(select)
                sauvegarder(revenus, depenses)
                print("Votre montant à bien été ajouté")
                pm = True

    if select == 2 :

        catégorie = input("Choisir une catégorie")

        pm = False
        while not pm:
            select = input("Tu as choisi l'option (Ajouter une dépense) !\nChoisir un montant !")
            if not select.isdigit():
                print("Invalid Input")
                continue
            select = int(select)

            if select < 0:
                print("Invalid Input")
                continue

            else:
                if catégorie in depenses :
                    depenses[catégorie].append(select)
                else :
                    depenses[catégorie] = [select]
                    sauvegarder(revenus, depenses)
                    print("Votre dépense à bien été ajoutée")
                    pm = True

    if select == 3 :
        total_revenus = sum_revenus(revenus)
        total_depenses = sum_depenses(depenses)
        total_économie = sum_économie(total_revenus,total_depenses)
        max_depense,nom = catégorie_plus(total_depenses)
        afficher_résumé(total_revenus,total_depenses,total_économie,nom)

    if select == 4:
        for categorie in depenses:
            print(f"{categorie} :")

            total_categorie = 0
            for montant in depenses[categorie]:
                print(f"- {montant} €")
                total_categorie += montant

            print(f"Total {categorie}: {total_categorie} €")
            print()




def sum_revenus(revenus):
    somme = 0
    for i in revenus :
        somme = somme + i
    return somme

def sum_depenses(depenses) :
    somme = 0
    for categorie in depenses :
        somme = somme + sum(depenses[categorie])
    return somme

def sum_économie(revenus,depenses) :
    économie = revenus - depenses
    if économie < 0 :
        print("Attention, tu dépenses plus que tes revenus")
        return économie
    return économie


def catégorie_plus(depenses) :
    max = 0
    nom  = ""
    for catégorie in depenses :
        total = sum(depenses[catégorie])
        if max < total:
            max = sum(depenses[catégorie])
            nom = catégorie
    return max,nom


if __name__ == "__main__":
    revenus, depenses = charger()

    running = True

    while running:
        select = menu()

        if select == 5:
            sauvegarder(revenus, depenses)
            print("Au revoir !")
            running = False
        else:
            ajout(select, revenus, depenses)
