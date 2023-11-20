import random

class Pacman:
    def __init__(self, position, board):
        self._position = position
        self._score = 0
        self._points_earned = 0
        self._board = board

    def move(self, direction):
        x, y = self._position
        new_x, new_y = x, y

        if direction == 'up':
            new_x -= 1
        elif direction == 'down':
            new_x += 1
        elif direction == 'left':
            new_y -= 1
        elif direction == 'right':
            new_y += 1

        # Ensure new_x is within bounds
        new_x = max(0, new_x)
        new_y = max(0, new_y)

        # Check if the new position is within bounds and not an obstacle
        if 0 <= new_x < len(self._board) and 0 <= new_y < len(self._board[0]) and self._board[new_x][new_y] != '#':
            # Check if Pac-Man eats a point
            if self._board[new_x][new_y] == '.':
                self._points_earned += 1  # Increment points_earned
                self._score += 10  # Update score based on points_earned
                self._board[new_x][new_y] = ' '  # Remove the point from the board

            # Update Pac-Man's position after checking for points
            self._position = (new_x, new_y)

        # Decrement score by 1 for each move
        self._score -= 1

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position

    def get_score(self):
        return self._score

    def get_points_earned(self):
        return self._points_earned

    def end_game(self, ghosts):
        if self._points_earned >= 100:
            print("Congratulations! You won the game.")
            exit()
        elif any(ghost._position == self._position for ghost in ghosts):
            print("Game over! Pac-Man was caught by a ghost.")
            exit()
        else:
            return None

