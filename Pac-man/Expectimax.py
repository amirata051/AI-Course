# Expectimax.py
from Ghost import Ghost
from Pacman import Pacman


class Expectimax:
    def __init__(self, pacman, ghosts, board):
        self.pacman = pacman
        self.ghosts = ghosts
        self.board = board

    def legal_moves(self):
        # Get all possible moves that are not towards the wall
        x, y = self.pacman._position
        possible_moves = ['up', 'down', 'left', 'right']

        legal_moves = []
        for move in possible_moves:
            new_x, new_y = x, y

            if move == 'up':
                new_x -= 1
            elif move == 'down':
                new_x += 1
            elif move == 'left':
                new_y -= 1
            elif move == 'right':
                new_y += 1

            # Check if the new position is within bounds and not an obstacle
            if 0 <= new_x < len(self.board) and 0 <= new_y < len(self.board[0]) and self.board[new_x][new_y] != '#':
                legal_moves.append(move)

        return legal_moves

    def expectimax_move(self, depth=3):
        possible_moves = self.legal_moves()

        move_utilities = {}
        for move in possible_moves:
            pacman_copy = Pacman(position=self.pacman.get_position(), board=self.board)
            pacman_copy.move(move)

            utility = self.expect_value(pacman_copy, self.ghosts, depth)
            move_utilities[move] = utility

        best_move = max(move_utilities, key=move_utilities.get)

        return best_move

    def max_value(self, pacman, ghosts, depth):
        if depth == 0 or pacman.end_game(ghosts):
            return self.evaluate_state(pacman, ghosts)

        max_utility = float('-inf')

        for move in ['up', 'down', 'left', 'right']:
            pacman_copy = Pacman(position=pacman.get_position(), board=self.board)
            pacman_copy.move(move)

            utility = self.expect_value(pacman_copy, ghosts, depth - 1)
            max_utility = max(max_utility, utility)

        return max_utility

    def expect_value(self, pacman, ghosts, depth):
        if depth == 0 or pacman.end_game(ghosts):
            return self.evaluate_state(pacman, ghosts)

        expect_utility = 0

        for ghost in ghosts:
            ghost_copy = Ghost(position=ghost.get_position(), board=self.board)
            ghost_copy.move()  # Random ghost move

            prob = 1 / len(ghosts)  # Dynamic probability for each ghost's move
            utility = self.max_value(pacman, [ghost_copy], depth - 1)
            expect_utility += prob * utility

        return expect_utility

    def evaluate_state(self, pacman, ghosts):
        # Criteria: 1. Pacman's score 2. Relative positions of Pacman and ghosts
        # 3. Distance to the nearest food pellet 4. Number of remaining food pellets
        # 5. Distance to the nearest ghost

        pacman_score_utility = pacman.get_score()

        # Check relative positions of Pacman and ghosts
        position_utility = sum(self.calculate_relative_position_utility(pacman, ghost) for ghost in ghosts)

        # Number of remaining food pellets
        remaining_food_utility = self.calculate_remaining_food_utility()

        # Distance to the nearest ghost
        nearest_ghost_utility = self.calculate_nearest_ghost_utility(pacman, ghosts)

        # Distance to the nearest point
        nearest_point_utility = self.calculate_nearest_point_utility(pacman)

        # Manhattan distance between two ghosts and Pacman
        distance_between_ghosts_utility = self.calculate_distance_between_pacma_and_ghosts_utility(pacman, ghosts)

        # Combine utilities with appropriate weights
        total_utility = (
                0.8 * pacman_score_utility +
                0.5 * position_utility +
                0.5 * remaining_food_utility +
                1.0 * nearest_point_utility +
                1.0 * nearest_ghost_utility +
                1.0 * distance_between_ghosts_utility
            # Adjust weights based on the importance of each feature
        )

        return total_utility

    def calculate_relative_position_utility(self, pacman, ghost):
        # Add your logic to evaluate the relative positions of Pacman and ghosts
        # For example, penalize if they are in a horizontal or vertical direction

        pacman_position = pacman.get_position()
        ghost_position = ghost.get_position()

        # Example logic: Penalize if Pacman and ghost are in the same row or column
        if pacman_position[0] == ghost_position[0] or pacman_position[1] == ghost_position[1]:
            return -1000  # Adjust the penalty as needed

        return 0  # No penalty if they are not in the same row or column

    def calculate_remaining_food_utility(self):
        # Add your logic to calculate the utility based on the number of remaining food pellets
        # For example, more remaining food can be rewarded

        remaining_food_count = sum(row.count('.') for row in self.board)

        return 5 * remaining_food_count  # Adjust the reward as needed

    def calculate_nearest_ghost_utility(self, pacman, ghosts):
        # Add your logic to calculate the distance to the nearest ghost
        # For example, penalize Pacman for being close to ghosts

        nearest_ghost_distance = min(
            abs(pacman.get_position()[0] - ghost.get_position()[0]) + abs(
                pacman.get_position()[1] - ghost.get_position()[1]
            ) for ghost in ghosts
        )

        return -500 / max(nearest_ghost_distance, 1)  # Adjust the penalty as needed

    def calculate_nearest_point_utility(self, pacman):
        nearest_point_distance = self.calculate_nearest_point_distance(pacman)
        return -20 * (nearest_point_distance + 1)  # Adjust the penalty as needed

    def calculate_nearest_point_distance(self, pacman):
        current_position = pacman.get_position()
        remaining_points = [(i, j) for i, row in enumerate(self.board) for j, cell in enumerate(row) if cell == '.']

        if not remaining_points:
            return 0  # No remaining points

        nearest_point_distance = min(
            abs(current_position[0] - point[0]) + abs(current_position[1] - point[1]) for point in remaining_points
        )

        return nearest_point_distance

    def calculate_distance_between_pacma_and_ghosts_utility(self, pacman, ghosts):
        # Your logic for calculating the Manhattan distance between two ghosts and Pacman
        # The output should encourage Pacman to move in a direction that increases this distance

        # Sample implementation (modify based on your specific criteria)
        if len(ghosts) < 2:
            return 0  # No distance to calculate

        ghost1, ghost2 = ghosts[:2]
        distance = abs(pacman.get_position()[0] - ghost1.get_position()[0]) + abs(
            pacman.get_position()[1] - ghost1.get_position()[1]) + abs(
            pacman.get_position()[0] - ghost2.get_position()[0]) + abs(
            pacman.get_position()[1] - ghost2.get_position()[1])

        return 10 * distance  # Adjust the reward as needed
