## main.py
import copy
import timeit
from PuzzleBoard import Cell,Clue,ClueCell,BlackCell,WhiteCell,Puzzle
from Agent import Agent
from IntelligentAgent import IntelligentAgent

WHITE = 0
CLUE = -1
BLACK = -2

DOWN = 'down'
RIGHT = 'right'
def reading_puzzle(data):
    # Split the data into rows
    rows = [row.strip('|').strip() for row in data.strip().split('\n')]

    # Initialize a 2D list to store the parsed entries
    entries = []

    # Iterate through each row and split into individual entries
    for row in rows:
        row_entries = [entry.strip() for entry in row.split('|')]
        entries.append(row_entries)

    cells = []
    # Display the parsed entries
    for i in range(len(entries)):
        for j in range(len(entries[0])):
            if entries[i][j] == '':
                continue
            elif entries[i][j] == 'X':
                cells.append(BlackCell((i, j)))
            elif entries[i][j][:1] == '\\':
                dc, rc = entries[i][j].split('\\')
                rc = int(rc)
                cells.append(ClueCell((i, j), None, Clue(RIGHT, entries[i].count(''), rc)))
            elif entries[i][j][-1:] == '\\':
                dc, rc = entries[i][j].split('\\')
                dc = int(dc)
                cells.append(ClueCell((i, j), Clue(DOWN, entries[:][j].count(''), dc), None))
            else:
                dc, rc = map(int, entries[i][j].split('\\'))
                cells.append(
                    ClueCell((i, j), Clue(DOWN, entries[:][j].count(''), dc), Clue(RIGHT, entries[i].count(''), rc)))

    return len(entries), len(entries[0]), cells


data0 = """
|   X  |  9\  |  11\  |
|  \\17 |      |       |
|  \\3  |      |       |
"""

data1 = """
|  X   | 17\  | 6\   |   X   |  X   |
|  \9  |      |      | 24\   |  X   |
|  \\20 |      |      |       | 4\   |
|  X   |  \\14 |      |       |      |
|  X   |  X   |  \8  |       |      |
"""

data2 = """
|   X   |   X   | 22\   | 12\   |   X   |
|   X   | 15\\12 |       |       |  9\   |
|  \\13  |       |       |       |       |
|  \\29  |       |       |       |       |
|   X   |  \\4   |       |       |   X   |
"""

dataset = [data0, data1, data2]
s = ''
for i in range(len(dataset)):
    h, w, cells = reading_puzzle(dataset[i])
    puzzle = Puzzle(h, w, cells)

    # unintelligent agent:
    unintelligent_agent = Agent(copy.deepcopy(puzzle))
    unintelligent_start = timeit.default_timer()
    unintelligent_agent.solve()
    unintelligent_stop = timeit.default_timer()
    unintelligent_time = unintelligent_stop - unintelligent_start

    # intelligent_agent:
    intelligent_agent = IntelligentAgent(copy.deepcopy(puzzle))
    intelligent_start = timeit.default_timer()
    intelligent_agent.solve()
    intelligent_stop = timeit.default_timer()
    intelligent_time = intelligent_stop - intelligent_start

    s += (f"Unintelligent agent solved puzzle {i + 1} in: {str(unintelligent_time)} sec\n")
    s += (f"Intelligent agent solved puzzle {i + 1} in: {str(intelligent_time)} sec\n\n")

print(s)