## IntelligentAgent.py
from Agent import Agent
from operator import itemgetter
class IntelligentAgent(Agent):
    def __init__(self, puzzle):
        super().__init__(puzzle)

    # Minimum Remaining Values (Most Constrained Variable) - chooses the clue with the least number of unassigned -
    # cells, but the clues that are already partially assigned are given priority
    def select_unallocated_clue(self, assignment):
        clue_list = []
        partial_assigned_list = []
        unassigned_list = []
        for clue in assignment.clues:
            if not assignment.is_clue_allocated(clue):
                unassigned_count = assignment.clue_unallocated_count(clue)
                if unassigned_count == clue.length:
                    unassigned_list.append((clue, unassigned_count))
                else:
                    partial_assigned_list.append((clue, unassigned_count))
        unassigned_list.sort(key=itemgetter(1))
        partial_assigned_list.sort(key=itemgetter(1))
        clue_list = partial_assigned_list + unassigned_list
        return clue_list[0][0]