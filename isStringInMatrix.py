def is_pattern_contained_in_grid(grid, pattern):
    def is_pattern_suffix_contained_starting_at_xy(x, y, offset):
        if len(pattern) == offset:
            return True

        if (not(0 <= x < len(grid) and 0 <= y < len(grid[x])) or grid[x][y] != pattern[offset] or (x, y, offset) in previous_attempts):
            return False

        if any(is_pattern_suffix_contained_starting_at_xy(x + a, y + b, offset + 1) for a, b in ((-1, 0), (1, 0), (0, -1), (0, 1))):
            return True

        previous_attempts.add((x, y, offset))
        return False

    previous_attempts = set()
    return any(is_pattern_suffix_contained_starting_at_xy(i, j, 0) for i in range(len(grid)) for j in range(len(grid[i])))

print(is_pattern_contained_in_grid([[1,2,3],[3,4,5],[5,6,7]], [1,3,4,6]))
print(is_pattern_contained_in_grid([[1,2,3],[3,4,5],[5,6,7]], [1,2,3,4]))
print(is_pattern_contained_in_grid([[1,2,3],[3,4,5],[5,6,7]], [1,3,4]))
print(is_pattern_contained_in_grid([[1,2,3],[3,4,5],[5,6,7]], [1,3,6]))