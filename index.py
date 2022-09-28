player = "X"
enemy = "O"
size = 0

def turn(who):
    turnActive = True
    while turnActive == True:
        i = input("Where would you like to place your " + who + "? ")
        if (i.isnumeric()):
            if (int(i) <= len(gamefield) and int(i) >= 0):
                if (gamefield[int(i) - 1] == "_" or gamefield[int(i) - 1] == " "):
                    gamefield[int(i) - 1] = who
                    turnActive = False
                else:
                    print("That spot is already taken!")
            else:
                print("Enter a number 1 - " + str(len(gamefield)) + ".")
        else:
            print("Enter a valid number.")

def buildField(gameArray):
    string = ""
    topRow = 0
    loopFinish = False
    for i in range(len(gameArray)):
        if (i!=0 and i!=1):
            if(len(gameArray) / i == i and loopFinish == False):
                loopFinish = True
                topRow = i

    index = 0
    for i in gameArray:
        if (index % topRow == 0):
            index += 1
            string = string + "\n" + i
        else:
            string = string + "|" + i
            index += 1
    string = string + "\n"
    print(string)

invalidArrayR = []
invalidArrayL = []
def checkForWin(gameArray, user):
    topRow = 0
    loopFinish = False
    for i in range(len(gameArray)):
        if (i!=0 and i!=1):
            if(len(gameArray) / i == i and loopFinish == False):
                loopFinish = True
                topRow = i

    for i in range(len(gameArray)):
        #vertical
        if (i / topRow < topRow - 2):
            if (gameArray[i] == user and gameArray[i + topRow] == user and gameArray[i + topRow * 2] == user):
                print("\033[92m" + user + " won!\033[0m")
                return True

        #horizontal
        if ((i + 1) % topRow == 0):
            if (not invalidArrayR.__contains__(i)):
                invalidArrayR.append(i - 1)
                invalidArrayR.append(i)
        if (not invalidArrayR.__contains__(i)):
            if (gameArray[i] == user and gameArray[i + 1] == user and gameArray[i + 2] == user):
                print("\033[92m" + user + " won!\033[0m")
                return True
        
        #diagonal
        if (not invalidArrayR.__contains__(i)):
            if (i / topRow < topRow - 2):
                if (gameArray[i] == user and gameArray[i + topRow + 1] == user and gameArray[i + topRow * 2 + 2] == user):
                    print("\033[92m" + user + " won!\033[0m")
                    return True
        if (i % topRow == 0):
            if (not invalidArrayL.__contains__(i)):
                invalidArrayL.append(i)
                invalidArrayL.append(i + 1)
        if (not invalidArrayL.__contains__(i)):
            if (i / topRow < topRow - 2):
                if (gameArray[i] == user and gameArray[i + topRow - 1] == user and gameArray[i + topRow * 2 - 2] == user):
                    print("\033[92m" + user + " won!\033[0m")
                    return True

while True:
    win = False
    gamefield = [
                "_", "_", "_",
                "_", "_", "_", 
                " ", " ", " ",
                ]

    #add horizontal fields
    for i in range(size):
        for i in range(2):
            gamefield.insert(0,"_")
        gamefield.insert(len(gamefield) - 1," ")

    #add vertical fields
    for i in range(size):
        for j in range(size + 3):
            gamefield.insert(0,"_")

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
