import math
import collections

def is_valid_sudoku(partial_assignment):
    #return true if subarray
    #partial assignment[start_row:end_row][start_column:end_column] 
    #contains any duplicates in {1,2,...,len(partial assignment)};
    #otherwise return False

    def has_duplicate(block):
        block = list(filter(lambda x:x!=0, block))
        return len(block)!=len(set(block))

    n = len(partial_assignment)
    if any(has_duplicate([partial_assignment[i][j] for j in range(n)]) or has_duplicate([partial_assignment[j][i] for j in range(n)]) for i in range(n)):
        return False

    #check region constraints
    region_size = int(math.sqrt(n))
    return all(not has_duplicate([partial_assignment[a][b] for a in range(region_size * I, region_size * (I+1)) for b in range(region_size * J, region_size * (J+1))]) for I in range(region_size) for J in range(region_size))

#Pythonic solution that exploits the power of list comprehension
#def is_valid_sudoku_pythonic(partial_assignment):
 #   region_size = int(math.sqrt(len(partial_assignment)))
  #  return max(collections.Counter(k for i, row in enumerate(partial_assignment) for j, c in enumerate(row) if c!=0 for k in ((i, str(c)), (str(c), j), (i // region_size, j // region_size, str(c)))). values(), default=0)<=1

print(is_valid_sudoku([[5,3,4,6,7,8,9,1,2], [6,7,2,1,9,5,3,4,8], [1,9,8,3,4,2,5,6,7], [8,5,9,7,6,1,4,2,3], [4,2,6,8,5,3,7,9,1], [7,1,3,9,2,4,8,5,6], [9,6,1,5,3,7,2,8,4], [2,8,7,4,1,9,6,3,5], [3,4,5,2,8,6,1,7,9]]))
print(is_valid_sudoku([[5,3,4,6,7,8,9,1,2], [6,7,2,1,9,5,3,4,8], [1,9,8,3,4,2,5,6,7], [8,5,9,7,6,1,4,2,3], [4,2,6,8,5,3,7,9,1], [7,1,3,9,2,4,8,5,6], [9,6,1,5,3,7,2,8,4], [2,8,7,4,1,9,6,3,5], [3,4,5,2,8,6,1,7,8]]))