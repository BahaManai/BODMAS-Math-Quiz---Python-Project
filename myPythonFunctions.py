#Tâche 1
import random
import os

#Tâche 2
def getUserPoint(nom):
    if not os.path.exists('userScores.txt'):
        with open('userScores.txt', 'w') as file:
            file.write("")
    with open('userScores.txt', 'r') as file:
        for line in file:
            utilisateur, score = line.strip().split(', ')
            if utilisateur == nom:
                return score
    return "-1"

#Tâche 3
def updateUserPoints(newUser, userName, score):
    score = str(score)
    if newUser:
        with open('userScores.txt', 'a') as file:
            file.write(userName+", "+score+"\n")
    else:
        with open('userScores.txt', 'r') as file, open('tempScores.txt', 'w') as temp_file:
            for line in file:
                name, sc = line.strip().split(', ')
                if name == userName:
                    sc = score
                temp_file.write(name+", "+sc+"\n")
        os.remove('userScores.txt')
        os.rename('tempScores.txt', 'userScores.txt')

#Tâche 4
def generateQuestion():
    operandList = [0,0,0,0,0]
    operatorList = ["","","","",""]
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
    operatorList = [operatorDict[random.randint(1, 4)]]
    for i in range(3):
        operator = operatorDict[random.randint(1, 4)]
        while operator == "**" and operatorList[-1] == "**":
            operator = operatorDict[random.randint(1, 4)]
        operatorList.append(operator)

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



