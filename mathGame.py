import myPythonFunctions

try:
    print("Bienvenue dans le jeu de mathématiques BODMAS!")
    print("Répondez aux questions et accumulez des points.")
    print("Tapez '-1' à tout moment pour quitter le jeu.")
    print("=" * 50)
    userName = input("Entrer votre nom : ")
    userScore = int(myPythonFunctions.getUserPoint(userName))
    if userScore == -1:
        newUser = True
        userScore = 0
        print("Bonjour "+userName+", il semble que vous êtes un nouveau joueur. Bon jeu!")
    else:
        newUser = False
        print("Bonjour "+userName+", votre score actuel est "+str(userScore)+" points.")
    print("=" * 50)
    
    userChoice = "0"
    while userChoice != "-1":
        result = myPythonFunctions.generateQuestion()
        userScore += result
        print("Votre score est "+str(userScore)+" points.")
        userChoice = input("Entrez '-1' pour quitter, sinon appuyez sur Entrée pour une nouvelle question : ")
    myPythonFunctions.updateUserPoints(newUser, userName, userScore)
    print("=" * 50)
    print("Merci d'avoir joué "+str(userName)+"! Votre score final est "+str(userScore)+" points.")
    print("À bientôt pour une nouvelle partie!")
    print("=" * 50)
except Exception as error:
    print("Une erreur s'est produite : "+str(error)+"\nLe programme va se fermer.")


