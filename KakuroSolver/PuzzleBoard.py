## PuzzleBoard.py

WHITE = 0
CLUE = -1
BLACK = -2

DOWN = 'down'
RIGHT = 'right'

class Cell:
    def __init__(self, location, category):
        self.location = location
        self.category = category


class Clue:
    def __init__(self, direction, length, goal_sum):
        self.direction = direction
        self.length = length
        self.goal_sum = goal_sum
        self.location = None


class ClueCell(Cell):
    def __init__(self, location, down_clue, right_clue):
        super().__init__(location, category=CLUE)
        self.down_clue = down_clue
        if down_clue is not None:
            self.down_clue.location = self.location
        self.right_clue = right_clue
        if right_clue is not None:
            self.right_clue.location = self.location


class BlackCell(Cell):
    def __init__(self, location):
        super().__init__(location, category=BLACK)


class WhiteCell(Cell):
    def __init__(self, location, value=0):
        super().__init__(location, category=WHITE)
        self.value = value


# create a kakuro puzzle class that specifies puzzle size, clues (the goal sums) and the black cells
class Puzzle:
    def __init__(self, height, width, cells):
        self.height = height
        self.width = width
        self.cells = cells
        self.clues = self.make_clues()
        self.puzzle = self.make_puzzle()
        self.print_puzzle()

    def print_puzzle(self):
        for i in range(self.height):
            for j in range(self.width):
                print("|", end="")
                cell = self.puzzle[i][j]
                if cell.category is BLACK:
                    print(f"   X   ", end="")
                elif cell.category is CLUE:
                    if cell.down_clue == None:
                        print(f'   \{cell.right_clue.goal_sum if cell.right_clue.goal_sum>9 else " "+str(cell.right_clue.goal_sum)} ', end="")
                    elif cell.right_clue == None:
                        print(f' {cell.down_clue.goal_sum if cell.down_clue.goal_sum>9 else " "+str(cell.down_clue.goal_sum)}\   ', end="")
                    else:
                        print(f' {cell.down_clue.goal_sum if cell.down_clue.goal_sum>9 else " "+str(cell.down_clue.goal_sum)}\{cell.right_clue.goal_sum if cell.right_clue.goal_sum>9 else " "+str(cell.right_clue.goal_sum)} ', end="")
                elif cell.category is WHITE:
                    print(f'   {cell.value}   ', end="")
            print("|")

        print("\n\n\n\n")

    def make_clues(self):
        clues = []
        for cell in self.cells:
            if cell.category == CLUE:
                if cell.down_clue is not None:
                    clues.append(cell.down_clue)
                if cell.right_clue is not None:
                    clues.append(cell.right_clue)
        return clues

    def make_puzzle(self):
        puzzle = [[WhiteCell((i, j)) for j in range(self.width)] for i in range(self.height)]
        for cell in self.cells:
            puzzle[cell.location[0]][cell.location[1]] = cell
        return puzzle

    def get_cell_set(self, clue):
        cell_set = []
        if clue.direction is DOWN:
            for i in range(clue.length):
                cell_set.append(self.puzzle[clue.location[0] + i + 1][clue.location[1]])
        elif clue.direction is RIGHT:
            for i in range(clue.length):
                cell_set.append(self.puzzle[clue.location[0]][clue.location[1] + i + 1])
        return cell_set

    def allocate_clue(self, clue, value_set):
        if clue.direction is DOWN:
            for i in range(clue.length):
                self.puzzle[clue.location[0] + i + 1][clue.location[1]].value = value_set.pop(0)
        elif clue.direction is RIGHT:
            for i in range(clue.length):
                self.puzzle[clue.location[0]][clue.location[1] + i + 1].value = value_set.pop(0)

    def is_clue_allocated(self, clue):
        return self.clue_unallocated_count(clue) == 0

    def clue_unallocated_count(self, clue):
        cell_set = self.get_cell_set(clue)
        unassigned_count = 0
        for cell in cell_set:
            if cell.value == 0:
                unassigned_count += 1
        return unassigned_count

    def completeness(self):
        is_complete = True
        for i in range(self.height):
            for j in range(self.width):
                if self.puzzle[i][j].category == WHITE and self.puzzle[i][j].value == 0:
                    is_complete = False
        return is_complete

    def compatibility(self):
        for clue in self.clues:
            cell_set = self.get_cell_set(clue)
            if self.is_clue_allocated(clue):
                current_sum = 0
                values = []
                for cell in cell_set:
                    values.append(cell.value)
                    current_sum += cell.value
                if current_sum != clue.goal_sum or any(values.count(x) > 1 for x in values):
                    return False
        return True