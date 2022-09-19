#input/output -> 1 = True = Black
#input/output -> 0 = False = White

import collections

def flip_color(x, y, image):
    color = image[x][y]
    q = collections.deque([(x, y)])
    image[x][y] = not image[x][y]

    while q:
        x, y = q.popleft()
        for next_x, next_y in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)):
            if (0 <= next_x < len(image) and 0 <= next_y < len(image[next_x]) and image[next_x][next_y] == color):
                image[next_x][next_y] = not image[next_x][next_y]
                q.append((next_x, next_y))

    return image

image = [[1,0,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,0,1,1],[1,1,1,0,0,1,1,0,1,1],[0,1,0,1,1,1,1,0,1,0],[1,0,1,0,0,0,0,1,0,0],[1,0,1,0,0,1,0,1,1,1],[0,0,0,0,1,0,1,0,0,1],[1,0,1,0,1,0,1,0,0,0],[1,0,1,1,0,0,0,1,1,1],[0,0,0,0,0,0,0,1,1,0]]

print(flip_color(5, 4, image))