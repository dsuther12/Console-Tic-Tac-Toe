#Created by: Dylan Suther, 8/20/2021
#Inspired by: 'A Tic Tac Toe Board' program in 'Automate the Boring Stuff with Python' by Al Sweigart

gameBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + ' |' + board['top-M'] + ' |' + board['top-R'])
    print('--+--+--')
    print(board['mid-L'] + ' |' + board['mid-M'] + ' |' + board['mid-R'])
    print ('--+--+--')
    print(board['low-L'] + ' |' + board['low-M'] + ' |' + board['low-R'])

def mainGame():
    turn = 'X'
    for i in range(9): # Range is 9 due to how many spaces are on a tic-tac-toe board
        printBoard(gameBoard)
        print('Turn for player ' + turn + '. Which space would you like to move on?')
        print('(E.g. top-L, mid-M, low-R)')
        move = input() # Player inputs a move


        # Checks if player tries to insert a move that doesn't exist on the board
        while move not in gameBoard.keys():
            print('Not a valid move player ' + turn + ', please try again.')
            print('(E.g. top-L, mid-M, low-R)')
            printBoard(gameBoard)
            move = input()

        # Checks if player tries to use a move that has already been taken
        while(gameBoard[move] != ' '):
            print('Space already filled, try again')
            printBoard(gameBoard)
            print('Turn for player ' + turn + '. Which space would you like to move on?')
            move = input()

        gameBoard[move] = turn # Replaces value of key with whatever player took the turn

        # Switches between players
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        # Each possible winning move in the game of tic-tac-toe
        if (gameBoard['top-L'] == 'X' and gameBoard['top-M'] == 'X' and gameBoard['top-R'] == 'X'):
            print('Player X wins!')
            break
        if (gameBoard['top-L'] == 'O' and gameBoard['top-M'] == 'O' and gameBoard['top-R'] == 'O'):
            print('Player O wins!')
            break
        if (gameBoard['mid-L'] == 'X' and gameBoard['mid-M'] == 'X' and gameBoard['mid-R'] == 'X'):
            print('Player X wins!')
            break
        if (gameBoard['mid-L'] == 'O' and gameBoard['mid-M'] == 'O' and gameBoard['mid-R'] == 'O'):
            print('Player O wins!')
            break
        if (gameBoard['low-L'] == 'X' and gameBoard['low-M'] == 'X' and gameBoard['low-R'] == 'X'):
            print('Player X wins!')
            break
        if (gameBoard['low-L'] == 'O' and gameBoard['low-M'] == 'O' and gameBoard['low-R'] == 'O'):
            print('Player O wins!')
            break
        if (gameBoard['top-L'] == 'X' and gameBoard['mid-L'] == 'X' and gameBoard['low-L'] == 'X'):
            print('Player X wins!')
            break
        if (gameBoard['top-L'] == 'O' and gameBoard['mid-L'] == 'O' and gameBoard['low-L'] == 'O'):
            print('Player O wins!')
            break
        if (gameBoard['top-M'] == 'X' and gameBoard['mid-M'] == 'X' and gameBoard['low-M'] == 'X'):
            print('Player X wins!')
            break
        if (gameBoard['top-M'] == 'O' and gameBoard['mid-M'] == 'O' and gameBoard['low-M'] == 'O'):
            print('Player O wins!')
            break
        if (gameBoard['top-R'] == 'X' and gameBoard['mid-R'] == 'X' and gameBoard['low-R'] == 'X'):
            print('Player X wins!')
            break
        if (gameBoard['top-R'] == 'O' and gameBoard['mid-R'] == 'O' and gameBoard['low-R'] == 'O'):
            print('Player O wins!')
            break
        if (gameBoard['top-R'] == 'X' and gameBoard['mid-M'] == 'X' and gameBoard['low-L'] == 'X'):
            print('Player X wins!')
            break
        if (gameBoard['top-R'] == 'O' and gameBoard['mid-M'] == 'O' and gameBoard['low-L'] == 'O'):
            print('Player O wins!')
            break
        if (gameBoard['top-L'] == 'X' and gameBoard['mid-M'] == 'X' and gameBoard['low-R'] == 'X'):
            print('Player X wins!')
            break
        if (gameBoard['top-L'] == 'O' and gameBoard['mid-M'] == 'O' and gameBoard['low-R'] == 'O'):
            print('Player O wins!')
            break

    printBoard(gameBoard)
    print('Would you like to play again? (Y/y) or (N/n).')

# Calls upon the main game function in order to play
mainGame()

# Asks the players if they would like to play again
resume = True
while resume == True:
    playAgain = input()
    if playAgain == 'Y' or playAgain == 'y':
        gameBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
        mainGame()
    else:
        resume == False
        print('Thanks for playing! Goodbye!')
        break
