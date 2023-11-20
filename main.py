import random
from Pacman import Pacman
from Ghost import Ghost
from GameBoard import GameBoard
from Expectimax import Expectimax
from Minimax import Minimax
import time
import os

# Global game board definition
board = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '.', '#', '.', '#', '#', '#', '#', '#', '#', '.', '#', '.', '#', '#', '.', '#'],
    ['#', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '#'],
    ['#', '.', '#', '.', '#', '#', '.', '#', '#', ' ', ' ', '#', '#', '.', '#', '#', '.', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#', ' ', ' ', ' ', ' ', '#', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '.', '#'],
    ['#', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '#'],
    ['#', '.', '#', '#', '.', '#', '.', '#', '#', '#', '#', '#', '#', '.', '#', '.', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

pacman = Pacman(position=(9, 1), board=board)
ghosts = [Ghost(position=(6, 10), board=board), Ghost(position=(6, 11), board=board)]

# Create instance
game_board = GameBoard(pacman, ghosts, board)
minimax = Minimax(pacman, ghosts, board)
expectimax = Expectimax(pacman, ghosts, board)

choice = int(input('Choose one Algorithm 1-Minimax, 2-Expectimax :'))
if choice == 1:
    while True:
        os.system('cls')
        # time.sleep(0.1)

        # Display the current state
        game_board.display()

        # Generate a direction using Minimax
        minimax_direction = minimax.minimax_move()
        pacman.move(minimax_direction)

        # expectimax_direction = expectimax.expectimax_move()
        # pacman.move(expectimax_direction)

        # random_direction = random.choice(['up', 'down', 'left', 'right'])
        # print(f"Pac-Man's random direction: {random_direction}")
        # pacman.move(random_direction)

        print(f'Pacman Score : {game_board.score()}')

        # Ghosts move randomly
        for ghost in ghosts:
            ghost.move()

        result = pacman.end_game(ghosts)
        if result is not None:
            break
        result = game_board.end_game()
        if result is not None:
            break
elif choice == 2:
    while True:
        os.system('cls')
        # time.sleep(0.1)

        # Display the current state
        game_board.display()

        # Generate a direction using Minimax
        # minimax_direction = minimax.minimax_move()
        # pacman.move(minimax_direction)

        expectimax_direction = expectimax.expectimax_move()
        pacman.move(expectimax_direction)

        # random_direction = random.choice(['up', 'down', 'left', 'right'])
        # print(f"Pac-Man's random direction: {random_direction}")
        # pacman.move(random_direction)

        print(f'Pacman Score : {game_board.score()}')

        # Ghosts move randomly
        for ghost in ghosts:
            ghost.move()

        result = pacman.end_game(ghosts)
        if result is not None:
            break
        result = game_board.end_game()
        if result is not None:
            break

print(f'Pacman Score : {game_board.score()}')

