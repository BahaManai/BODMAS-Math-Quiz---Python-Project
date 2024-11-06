#Tâche 1
import random
import os

#Tâche 2
def getUserPoint(nom):
    L = []
    if not os.path.exists('userScores.txt'):
        file = open('userScores.txt', 'w')
        file.write("")
        file.close()

    file = open('userScores.txt', 'r')
    for line in file:
        utilisateur, score = line.strip().split(', ')
        L.append((utilisateur, int(score)))
        if utilisateur == nom:
            file.close()
            return score
    file.close()
    return "-1"

#Tâche 3
def updateUserPoints(newUser, userName, score):
    score = str(score)
    if newUser:
        file = open('userScores.txt', 'a')
        file.write(userName + ", " + score + "\n")
        file.close()
    else:
        file = open('userScores.txt', 'r')
        temp_file = open('tempScores.txt', 'w')
        for line in file:
            name, sc = line.strip().split(', ')
            if name == userName:
                sc = score
            temp_file.write(name + ", " + sc + "\n")
        file.close()
        temp_file.close()
        os.remove('userScores.txt')
        os.rename('tempScores.txt', 'userScores.txt')

#Tâche 4
def generateQuestion():
    operandList = [0,0,0,0,0]
    operatorList = ["","","",""]
    operatorDict = {
        1: "+",
        2: "-",
        3: "*",
        4: "**"
    }

    #Action 4.1
    for i in range(5):
        operandList = [random.randint(1, 9) for i in range(5)]

    #Action 4.2
    operatorList[0] = operatorDict[random.randint(1, 4)]
    for i in range(1, 4):
        operator = operatorDict[random.randint(1, 4)]
        while operator == "**" and operatorList[i - 1] == "**":
            operator = operatorDict[random.randint(1, 4)]
        operatorList[i] = operator

    #Action 4.3
    questionString = ""
    for i in range(4):
        questionString += str(operandList[i]) + " " + operatorList[i] + " "
    questionString += str(operandList[4])

    #Action 4.4
    result = eval(questionString)

    #Action 4.5
    questionString = questionString.replace("**","^")
    while True:
            try:
                reponse = int(input("Quel est le résultat de cette opération ?\n"+questionString+" = "))
                if reponse == result:
                    print("Bravo ! Votre réponse est correcte.")
                    return 1
                else:
                    print("Dommage ! Fausse réponse. Le résultat est : "+str(result))
                    return 0
            except ValueError:
                print("Veuillez entrer un entier !")