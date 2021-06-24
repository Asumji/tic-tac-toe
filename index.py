gamefield = "_|_|_\n_|_|_\n | | "
player = "X"
enemy = "O"


print(gamefield)
def playerTurn():
    i = input("Where would you like to place your X? ")
    
    if i.isnumeric():
        i = int(i)
        if i > 0 and i < 10:
            global gamefield
            if (i == 1):
                if (gamefield[0] == "_"):
                        tempField = list(gamefield)
                        tempField[0] = "X"
                        tempField = "".join(tempField)

                        gamefield = tempField
                        print(gamefield)
            elif (i == 2):
                if (gamefield[2] == "_"):
                    tempField = list(gamefield)
                    tempField[2] = "X"
                    tempField = "".join(tempField)

                    gamefield = tempField
                    print(gamefield)
            elif (i == 3):
                if (gamefield[4] == "_"):
                    tempField = list(gamefield)
                    tempField[4] = "X"
                    tempField = "".join(tempField)

                    gamefield = tempField
                    print(gamefield)
            elif (i == 4):
                if (gamefield[6] == "_"):
                    tempField = list(gamefield)
                    tempField[6] = "X"
                    tempField = "".join(tempField)

                    gamefield = tempField
                    print(gamefield)
            elif (i == 5):
                if (gamefield[8] == "_"):
                    tempField = list(gamefield)
                    tempField[8] = "X"
                    tempField = "".join(tempField)

                    gamefield = tempField
                    print(gamefield)
            elif(i == 6):
                if (gamefield[10] == "_"):
                    tempField = list(gamefield)
                    tempField[10] = "X"
                    tempField = "".join(tempField)

                    gamefield = tempField
                    print(gamefield)
            elif (i == 7):
                if (gamefield[12] == " "):
                    tempField = list(gamefield)
                    tempField[12] = "X"
                    tempField = "".join(tempField)

                    gamefield = tempField
                    print(gamefield)
            elif (i == 8):
                if (gamefield[14] == " "):
                    tempField = list(gamefield)
                    tempField[14] = "X"
                    tempField = "".join(tempField)

                    gamefield = tempField
                    print(gamefield)
            elif (i == 9):
                if (gamefield[16] == " "):
                    tempField = list(gamefield)
                    tempField[16] = "X"
                    tempField = "".join(tempField)

                    gamefield = tempField
                    print(gamefield)
        else:
            print("You entered a number which is too high/too low! (1 - 9)")
    else:
        print("You did not enter a number!")

def enemyTurn():
    i = input("Where would you like to place your O? ")
    
    if i.isnumeric():
        i = int(i)
        if i > 0 and i < 10:
            global gamefield
            if (i == 1):
                if (gamefield[0] == "_"):
                        tempField = list(gamefield)
                        tempField[0] = "O"
                        tempField = "".join(tempField)

                        gamefield = tempField
                        print(gamefield)
            elif (i == 2):
                if (gamefield[2] == "_"):
                    tempField = list(gamefield)
                    tempField[2] = "O"
                    tempField = "".join(tempField)

                    gamefield = tempField
                    print(gamefield)
            elif (i == 3):
                if (gamefield[4] == "_"):
                    tempField = list(gamefield)
                    tempField[4] = "O"
                    tempField = "".join(tempField)

                    gamefield = tempField
                    print(gamefield)
            elif (i == 4):
                if (gamefield[6] == "_"):
                    tempField = list(gamefield)
                    tempField[6] = "O"
                    tempField = "".join(tempField)

                    gamefield = tempField
                    print(gamefield)
            elif (i == 5):
                if (gamefield[8] == "_"):
                    tempField = list(gamefield)
                    tempField[8] = "O"
                    tempField = "".join(tempField)

                    gamefield = tempField
                    print(gamefield)
            elif(i == 6):
                if (gamefield[10] == "_"):
                    tempField = list(gamefield)
                    tempField[10] = "O"
                    tempField = "".join(tempField)

                    gamefield = tempField
                    print(gamefield)
            elif (i == 7):
                if (gamefield[12] == " "):
                    tempField = list(gamefield)
                    tempField[12] = "O"
                    tempField = "".join(tempField)

                    gamefield = tempField
                    print(gamefield)
            elif (i == 8):
                if (gamefield[14] == " "):
                    tempField = list(gamefield)
                    tempField[14] = "O"
                    tempField = "".join(tempField)

                    gamefield = tempField
                    print(gamefield)
            elif (i == 9):
                if (gamefield[16] == " "):
                    tempField = list(gamefield)
                    tempField[16] = "O"
                    tempField = "".join(tempField)

                    gamefield = tempField
                    print(gamefield)
        else:
            print("You entered a number which is too high/too low! (1 - 9)")
    else:
        print("You did not enter a number!")
    
win = False
while win == False:
    playerTurn()
    
    tempField = gamefield
    tempField = tempField.replace("\n", "")
    tempField = tempField.replace("|", "")

    if (tempField[0] == "X" and tempField[3] == "X" and tempField[6] == "X"):
        win = True
        break

    if (tempField[1] == "X" and tempField[4] == "X" and tempField[7] == "X"):
        win = True
        break

    if (tempField[2] == "X" and tempField[5] == "X" and tempField[8] == "X"):
        win = True
        break

    if (tempField[0] == "X" and tempField[1] == "X" and tempField[2] == "X"):
        win = True
        break

    if (tempField[3] == "X" and tempField[4] == "X" and tempField[5] == "X"):
        win = True
        break

    if (tempField[6] == "X" and tempField[7] == "X" and tempField[8] == "X"):
        win = True
        break

    if (tempField[0] == "X" and tempField[4] == "X" and tempField[8] == "X"):
        win = True
        break

    if (tempField[6] == "X" and tempField[4] == "X" and tempField[2] == "X"):
        win = True
        break

    count = 0
    for i in tempField:
        if (i == "_" or i == " "):
            count += 1

    if count == 0:
        print("Draw!")
        break

    enemyTurn()

    if (tempField[0] == "O" and tempField[3] == "O" and tempField[6] == "O"):
        win = True
        break

    if (tempField[1] == "O" and tempField[4] == "O" and tempField[7] == "O"):
        win = True
        break

    if (tempField[2] == "O" and tempField[5] == "O" and tempField[8] == "O"):
        win = True
        break

    if (tempField[0] == "O" and tempField[1] == "O" and tempField[2] == "O"):
        win = True
        break

    if (tempField[3] == "O" and tempField[4] == "O" and tempField[5] == "O"):
        win = True
        break

    if (tempField[6] == "O" and tempField[7] == "O" and tempField[8] == "O"):
        win = True
        break

    if (tempField[0] == "O" and tempField[4] == "O" and tempField[8] == "O"):
        win = True
        break

    if (tempField[6] == "O" and tempField[4] == "O" and tempField[2] == "O"):
        win = True
        break

    count = 0
    for i in tempField:
        if (i == "_" or i == " "):
            count += 1

    if count == 0:
        print("Draw!")
        break

print("Game end!")