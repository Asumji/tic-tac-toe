player = "X"
enemy = "O"

def turn(who):
    turnActive = True
    while turnActive == True:
        i = input("Where would you like to place your " + who + "? ")
        if (i.isnumeric()):
            if (gamefield[int(i) - 1] == "_" or gamefield[int(i) - 1] == " "):
                gamefield[int(i) - 1] = who
                turnActive = False
            else:
                print("That spot is already taken!")
        else:
            print("Enter a number 1 - 9.")

def buildField(gameArray):
    string = ""
    index = 0
    for i in gameArray:
        if (index % 3 == 0):
            index += 1
            string = string + "\n" + i
        else:
            string = string + "|" + i
            index += 1
    string = string + "\n"
    print(string)

def checkForWin(gameArray, user):
    for i in range(9):
        #vertical
        if (i == 0 or i == 1 or i == 2):
            if (gameArray[i] == user and gameArray[i + 3] == user and gameArray[i + 6] == user):
                print("\033[92m" + user + " won!\033[0m")
                return True

        #horizontal
        if (i == 0 or i == 3 or i == 6):
            if (gameArray[i] == user and gameArray[i + 1] == user and gameArray[i + 2] == user):
                print("\033[92m" + user + " won!\033[0m")
                return True

        #diagonal
        if (i == 0):
            if (gameArray[i] == user and gameArray[i + 4] == user and gameArray[i + 8] == user):
                print("\033[92m" + user + " won!\033[0m")
                return True
        elif (i == 2):
            if (gameArray[i] == user and gameArray[i + 2] == user and gameArray[i + 4] == user):
                print(user + " won!")
                return True

while True:
    win = False
    gamefield = [
                "_", "_", "_",
                "_", "_", "_",
                " ", " ", " "
                ]
    buildField(gamefield)
    while win == False:
        if (not gamefield.__contains__("_") and not gamefield.__contains__(" ")):
            print("Draw!")
            win = True
            break
        turn(player)
        buildField(gamefield)
        if (checkForWin(gamefield, player)):
            win = True
            break
        if (not gamefield.__contains__("_") and not gamefield.__contains__(" ")):
            print("Draw!")
            win = True
            break
        turn(enemy)
        buildField(gamefield)
        if (checkForWin(gamefield, enemy)):
            win = True
            break
