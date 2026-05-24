def printBoard(xstate, zstate):

    def getSymbol(i):
        if xstate[i] == 1:
            return "X"
        elif zstate[i] == 1:
            return "O"
        else:
            return str(i)

    print(f"{getSymbol(0)} | {getSymbol(1)} | {getSymbol(2)}")
    print("--|---|--")
    print(f"{getSymbol(3)} | {getSymbol(4)} | {getSymbol(5)}")
    print("--|---|--")
    print(f"{getSymbol(6)} | {getSymbol(7)} | {getSymbol(8)}")


def checkwin(xstate, zstate):

    wins = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]             # diagonals
    ]

    for win in wins:

        if (xstate[win[0]] + xstate[win[1]] + xstate[win[2]] == 3):
            print("X wins!")
            return 1

        if (zstate[win[0]] + zstate[win[1]] + zstate[win[2]] == 3):
            print("O wins!")
            return 0

    return -1


# Initialize game
xstate = [0] * 9
zstate = [0] * 9

turn = 1   # 1 = X, 0 = O

print("Welcome to Tic Tac Toe")

while True:

    printBoard(xstate, zstate)

    if turn == 1:
        print("X's chance")
    else:
        print("O's chance")

    value = int(input("Enter position (0-8): "))

    # Check if position is already taken
    if xstate[value] == 1 or zstate[value] == 1:
        print("Position already taken!")
        continue

    # Assign move
    if turn == 1:
        xstate[value] = 1
    else:
        zstate[value] = 1

    # Check winner
    cwin = checkwin(xstate, zstate)

    if cwin != -1:
        printBoard(xstate, zstate)
        print("Match over")
        break

    # Change turn
    turn = 1 - turn