import random

class Ghost:
    def __init__(self, position, board):
        self._position = position
        self._board = board

    def move(self):
        x, y = self._position
        direction = random.choice(['up', 'down', 'left', 'right'])

        new_x, new_y = x, y
        if direction == 'up':
            new_x -= 1
        elif direction == 'down':
            new_x += 1
        elif direction == 'left':
            new_y -= 1
        elif direction == 'right':
            new_y += 1

        # Check if the new position is within bounds and not an obstacle
        if 0 <= new_x < len(self._board) and 0 <= new_y < len(self._board[0]) and self._board[new_x][new_y] != '#':
            self._position = (new_x, new_y)

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position
