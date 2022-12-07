board = ['-' for i in range(9)]
def display_board():

    print('|',board[0],'|',board[1],'|',board[2],'|')
    print('|',board[3],'|',board[4],'|',board[5],'|')
    print('|',board[6],'|',board[7],'|',board[8],'|')

player1 = 'X'
player2 = 'O'

def check_condition(player):
    condition = [
        [0,1,2],[3,4,5],[6,7,8],[0,3,6],
        [1,4,7],[2,5,8],[0,4,8],[2,4,6]
    ]
    for check in condition:
        if board[check[0]] == player and board[check[1]] == player and board[check[2]] == player:
            return 1
    else:
        return 0

def play():
    display_board()
    while True:
        while True:
            player1_option = int(input("X, Enter the position : "))

            if player1_option not in [i for i in range(1,10)]:
                print("Please enter (1-9)!")
                continue
            if board[player1_option - 1] == '-':
                board[player1_option - 1] = player1
                display_board()

                if check_condition(player1):
                    return "\t\t ******* WINNER IS [X] ******* "
                break

            else:
                print("This place is occupied!")

        if len([i for i in board if i == '-']) == 0:
                return "\t\t ******* MATCH TIE! *******"

        while True:
            player2_option = int(input("O, Enter your position : "))

            if player2_option not in [i for i in range(1,10)]:
                print("Please enter (1-9)")
                continue
            if board[player2_option - 1] == '-':
                board[player2_option - 1] = player2
                display_board()
                if check_condition(player2):
                    return "\t\t ******* WINNER IS [O] *******"
                break

            else:
                print("This place is occupied!")


print(play())

run = True
while run:
    again = input("If you want to play again [y/n] : ")
    if again in 'yY':
        board = ['-' for i in range(9)]
        play()
    else:
        print("\t\t ******* GOOD GAME! *******")
        run = False



