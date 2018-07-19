
#Board_Definition
board=[" "," "," "," "," "," "," "," "," "," "]

def show_board():
    print ("    |    |   ")
    print ("" +board[1]+ "   |" +board[2]+ "   |" +board[3]+ " ")
    print ("    |    |   ")
    print ("----|----|----")
    print ("    |    |   ")
    print ("" +board[4]+ "   |" +board[5]+ "   |" +board[6]+ " ")
    print ("    |    |   ")
    print ("----|----|----")
    print ("    |    |   ")
    print ("" +board[7]+ "   |" +board[8]+ "   |" +board[9]+ " ")
    print ("    |    |   ")

def start_play():
    while True:
        choice = input("Enter your choice(1-9): ")
        if choice!='' and choice!='q':
            choice = int(choice)
            if len(board[choice]) !=0:
                print('The square is not empty. Enter another choice')
            else:
                board[choice] = "X" 
                show_board()
        elif choice=='q':
            break

show_board()
start_play()
