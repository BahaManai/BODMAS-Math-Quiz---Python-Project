import myPythonFunctions

try:
    userName = input("Donner votre nom : ")
    userScore = int(myPythonFunctions.getUserPoint(userName))
    if userScore == -1:
        newUser = True
        userScore = 0
    else:
        newUser = False
    print("Bonjour "+str(userName)+", votre score est "+str(userScore)+".")
    userChoice = "0"
    while userChoice != "-1":
        result = myPythonFunctions.generateQuestion()
        userScore += result
        print("Votre score est "+str(userScore)+".")
        userChoice = input("Entrez '-1' pour quitter, sinon une nouvelle question : ")
    myPythonFunctions.updateUserPoints(newUser, userName, userScore)
    print(f"Merci d'avoir joué "+str(userName)+"! Votre score final est "+str(userScore)+".")
except Exception as error:
    print(f"Une erreur s'est produite : "+str(error)+"\nLe programme va se fermer.")


