def matrix_search(A, x):
    #Start from top-right corner
    row, col = 0, len(A[0]) - 1

    #Keep searching while there are unclassified rows and columns
    while row < len(A) and col >= 0:
        if A[row][col] == x:
            return x
        elif A[row][col] < x:
            row += 1
        else:
            col -= 1

    return False

A = [[-1,2,4,4,6],[1,5,5,9,21],[3,6,6,9,22],[3,6,8,10,24],[6,8,9,12,25],[8,10,12,13,40]]
print(matrix_search(A, 8))