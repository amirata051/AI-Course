class GameBoard:
    def __init__(self, pacman, ghosts, board):
        self.pacman = pacman
        self.ghosts = ghosts
        self.board = board

    def display(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if (i, j) == self.pacman.get_position():
                    print('P', end=' ')
                elif any(ghost.get_position() == (i, j) for ghost in self.ghosts):
                    print('G', end=' ')
                else:
                    print(self.board[i][j], end=' ')
            print()

    def remaining_points(self):
        count = 0
        for row in self.board:
            for cell in row:
                if cell == '.':
                    count += 1
        return count
    
    def score(self):
        return (100-self.remaining_points())*10 + self.pacman._score
    
    def end_game(self):
        if self.remaining_points() == 0:
            print("Congratulations! Pac-man won the game.")
            return 'win'
        elif any(ghost.get_position() == self.pacman.get_position() for ghost in self.ghosts):
            print("Game over! Pac-Man was caught by a ghost.")
            return 'loss'
        else:
            return None
    

