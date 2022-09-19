def minimum_path_weight(triangle):
    min_weight_to_curr_row = [0]

    for row in triangle:
        min_weight_to_curr_row = [row[j] + min(min_weight_to_curr_row[max(j - 1, 0)], min_weight_to_curr_row[min(j, len(min_weight_to_curr_row) - 1)]) for j in range(len(row))]

    return min(min_weight_to_curr_row)

print(minimum_path_weight([[2],[4, 4],[8, 5, 6],[4, 2, 6, 2],[1, 5, 2, 3, 4]]))