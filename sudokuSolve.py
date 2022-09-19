########!!!!!!!!!!!!!! Need to recheck this code for False condition !!!!!!!!!!!!!!########

import math
import itertools

def solve_sudoku(partial_assignment):
    def solve_partial_sudoku(i, j):
        if i == len(partial_assignment):
            i = 0 #Starts a row
            j += 1
            if j == len(partial_assignment[i]):
                return True #Entire matrix has been filled without conflict

        #Skips nonempty entries
        if partial_assignment[i][j] != empty_entry:
            return solve_partial_sudoku(i + 1, j)
        
        def valid_to_add(i, j, val):
            #Check row constraints
            if any(val == partial_assignment[k][j] for k in range(len(partial_assignment))):
                return False

            #Check column constraints
            if val in partial_assignment[i]:
                return False

            #Check region constraints
            region_size = int(math.sqrt(len(partial_assignment)))
            I = i //region_size
            J = j //region_size

            return not any(val == partial_assignment[region_size * I + a][region_size * J + b] for a, b in itertools.product(range(region_size), repeat=2))

        for val in range(1, len(partial_assignment) + 1):
            #Its substantially quicker to check if entry val with any of the 
            #constraints if we add it at (i, j) adding it, rather than adding it and
            #then checking all constraints. The reason is that we know we are 
            #starting with a valid configuration, and only entry which can 
            #cause a problem is entry val at (i, j)
            if valid_to_add(i, j, val):
                partial_assignment[i][j] = val
                if solve_partial_sudoku(i + 1, j):
                    return True

        partial_assignment[i][j] = empty_entry #Undo assignment
        return False

    empty_entry = 0
    return solve_partial_sudoku(0, 0)

print(solve_sudoku([[5,3,4,6,7,8,9,1,2], [6,7,2,1,9,5,3,4,8], [1,9,8,3,4,2,5,6,7], [8,5,9,7,6,1,4,2,3], [4,2,6,8,5,3,7,9,1], [7,1,3,9,2,4,8,5,6], [9,6,1,5,3,7,2,8,4], [2,8,7,4,1,9,6,3,5], [3,4,5,2,8,6,1,7,9]]))
print(solve_sudoku([[5,3,4,6,7,8,9,1,2], [6,7,2,1,9,5,3,4,8], [1,9,8,3,4,2,5,6,7], [8,5,9,7,6,1,4,2,3], [4,2,6,8,5,3,7,9,1], [7,1,3,9,2,4,8,5,6], [9,6,1,5,3,7,2,8,4], [2,8,7,4,1,9,6,3,5], [3,4,5,2,8,6,1,7,8]]))