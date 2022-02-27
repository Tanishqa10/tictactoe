  
state = [ # nested list 
    ["*","*","*"],#i0
    ["*","*","*"],
    ["*","*","*"]
]

def checkWin(x, y):
    for i in range(3):
        if x[i][0] == x[i][1] == x[i][2] == y:
            return y
        if x[0][i] == x[1][i] == x[2][i] == y:
            return y
    if x[0][0] == x[1][1] == x[2][2] == y:
        return y
    if x[0][2] == x[1][1] == x[2][0] == y:
        return y
    return 0

def gridDisplay(y):
    for i in y:
        for j in i:
            print(j, end=" ")
        print() # for new line`

turn = "X"

while True:
    gridDisplay(state)
    print(turn +"'s turn")
    row = int(input("Enter row number: "))
    col = int(input("Enter col number: "))
    if row>3 or col>3 or row<1 or col<1:
        print("Rows and Columns should be less than 4 or greater than 0!")
        continue
    if state[row - 1][col - 1] == "*":
        state[row - 1][col - 1] = turn
    else:
        print("Please Enter a valid row and column")
    winner = checkWin(state, turn)
    if winner != 0:
        print("Winner is", turn)
        break
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
