import random
def creation(select):
    digits = []
    name = input("What is your name bro !")

    if select == 1 :
     while len(digits) < 4:
        for i in range(4):
            pm = random.randint(0, 9)
            if pm not in digits:
                digits.append(pm)

    elif select == 2 :
        while len(digits) < 4:
            for i in range(4):
                pm = random.randint(0, 9)
                digits.append(pm)

    elif select == 3 :
        while len(digits) < 5:
            for i in range(5):
                pm = random.randint(0, 9)
                digits.append(pm)

    return digits,name


def selecting(select):
    real = True
    if select == 3 :
        while real:
            selection = input("Saisir un code de 5 chiffres : ")
            true_selection = list(selection)
            if len(set(true_selection)) != 5:
                print("Invalid value")
                continue




            else:
                true_selection = [int(x) for x in true_selection]
                real = False

    elif select == 2 :
        while real:
            selection = input("Saisir un code de 4 chiffres : ")
            true_selection = list(selection)
            if len(set(true_selection)) != 4:
                print("Invalid value")
                continue



            else:
                true_selection = [int(x) for x in true_selection]
                real = False

    elif select == 1 :
        while real:
            selection = input("Saisir un code de 4 chiffres : ")
            true_selection = list(selection)

            if len(set(true_selection)) != 4:
                print("Invalid value")
                continue
            for i in true_selection:
                if not i.isdigit():
                    print("Invalid value")
                    break


            else:
                true_selection = [int(x) for x in true_selection]
                real = False








    return true_selection


def game(digits,essais_max, select):

    essais = 0
    gagner = False

    while not gagner and essais <= essais_max:
        true_selection = selecting(select)
        count_true = 0
        count_false = 0

        for i in range(4):
            if true_selection[i] == digits[i]:
                count_true = count_true + 1

        for j in range(4):
            if digits[j] != true_selection[j] and true_selection[j] in digits:
                count_false = count_false + 1

        if count_true == 4 and count_false == 0  :
            gagner = True
        else:
            essais = essais + 1
        print(f"{count_true} chiffre(s) bien placé(s)\n{count_false} chiffre(s) mal placé(s)")

    return essais



def choix_niveaux() :
    select = int(input("Select your difficulty : (1-Easy) | (2-Medium) | (3-Hard) : "))
    essais_max = 0
    while not (1<=select<=3)  :
        print("Connard tu m'as donné un mauvais chiffre. Refais ! ")
        select = int(input("Select your difficulty : (1-Easy) | (2-Medium) | (3-Hard)"))
    if select == 1 :
        essais_max = 12
    elif select == 2 :
        essais_max = 10
    elif select == 3 :
        essais_max = 8
    return essais_max, select

def afficher_leaderboard():
    f = open("pm.txt","r")
    print(f.read())

def loading_score(name,essais,difficulty):
    f = open("pm.txt","a")
    f.write(f"\n{name} - {essais} essais - level {difficulty}")


if __name__=='__main__' :
    afficher_leaderboard()
    essais_max,select = choix_niveaux()
    digits,name = creation(select)
    essais = game(digits, essais_max, select)
    print(f"Bravo {name} tu as réussi à le faire en {essais} fois ")
    loading_score(name, essais, select)









