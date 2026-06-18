import random

def sauvegarder_score(name,essai):
    print(f" Good job {name}, it took you {essai} try")
    f = open("leaderboard.txt", "a")
    f.write(f"\n{name} - {essai} essais")


def afficher_leaderboard() :
    f = open("leaderboard.txt", "r")
    print(f.read())

def difficulty_choice():
    difficulty = int(input("Select your difficulty level (1-Easy : 2-Medium : 3-Hard) : "))
    name = input("What is your name : ")
    return difficulty,name

def play(difficulty) :
    find = False
    essai = 0
    if difficulty == 1:
        secret = random.randint(1, 50)
        max_essai = 10
        while not find:
            try:
                proposition = int(input("Select a number please : "))
            except:
                print("Please enter a valid integer")
            if proposition < 1 or proposition > 50:
                print("The number must be between 1 and 50")
                continue

            essai = essai + 1

            if essai > max_essai:
                break
            elif proposition < secret:
                print("To small !")

            elif proposition > secret:
                print("To big !")
            else:
                print("Good job ! ")
                find = True

    if difficulty == 2:
        secret = random.randint(1, 100)
        max_essai = 7
        while not find:
            try:
                proposition = int(input("Select a number please : "))
            except:
                print("Please enter a valid integer")
            if proposition < 1 or proposition > 100:
                print("The number must be between 1 and 100")
                continue

            essai = essai + 1

            if essai > max_essai:
                break
            elif proposition < secret:
                print("To small !")

            elif proposition > secret:
                print("To big !")
            else:
                print("Good job ! ")
                find = True

    if difficulty == 3:
        secret = random.randint(1, 200)
        max_essai = 5
        while not find:
            try:
                proposition = int(input("Select a number please : "))
            except:
                print("Please enter a valid integer")
            if proposition < 1 or proposition > 200:
                print("The number must be between 1 and 200")
                continue

            essai = essai + 1

            if essai > max_essai:
                break
            elif proposition < secret:
                print("To small !")

            elif proposition > secret:
                print("To big !")
            else:
                print("Good job ! ")
                find = True
    return essai





if __name__ == '__main__':
    afficher_leaderboard()
    difficulty,name = difficulty_choice()
    pm = int(input("Do you want to play (Yes-1 | 0-No) ?"))
    while pm==1 :
     essaie = play(difficulty)
     pm = int(input("Do you want to play again (Yes-1 | 0-No) ?"))
     sauvegarder_score(name,essaie)


