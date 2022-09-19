import collections

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

def search_maze(maze, s, e):
    def search_maze_helper(cur):
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x]) and maze[cur.x][cur.y] == WHITE):
            return False

        path.append(cur)
        maze[cur.x][cur.y] = BLACK

        if cur == e:
            return True

        if any(map(search_maze_helper, map(Coordinate, (cur.x - 1, cur.x + 1, cur.x, cur.x), (cur.y, cur.y, cur.y - 1, cur.y + 1)))):
            return True
        
        del path[-1]
        return False
        
    path = []
    search_maze_helper(s)
    return path

C00 = Coordinate(0, 0)
C01 = Coordinate(0, 1)
C02 = Coordinate(0, 2)
C03 = Coordinate(0, 3)
C10 = Coordinate(1, 0)
C11 = Coordinate(1, 1)
C12 = Coordinate(1, 2)
C13 = Coordinate(1, 3)
C20 = Coordinate(2, 0)
C21 = Coordinate(2, 1)
C22 = Coordinate(2, 2)
C23 = Coordinate(2, 3)
C30 = Coordinate(3, 0)
C31 = Coordinate(3, 1)
C32 = Coordinate(3, 2)
C33 = Coordinate(3, 3)

maze = [[0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0]]

print(search_maze(maze, C00, C30))