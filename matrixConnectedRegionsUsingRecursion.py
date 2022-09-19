def flip_color(x, y, image):
    color = image[x][y]
    image[x][y] = not image[x][y]

    for next_x, next_y in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)):
        if (0 <= next_x < len(image) and 0 <= next_y < len(image[next_x]) and image[next_x][next_y] == color):
            flip_color(next_x, next_y, image)

    return image

image = [[1,0,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,0,1,1],[1,1,1,0,0,1,1,0,1,1],[0,1,0,1,1,1,1,0,1,0],[1,0,1,0,0,0,0,1,0,0],[1,0,1,0,0,1,0,1,1,1],[0,0,0,0,1,0,1,0,0,1],[1,0,1,0,1,0,1,0,0,0],[1,0,1,1,0,0,0,1,1,1],[0,0,0,0,0,0,0,1,1,0]]

print(flip_color(5, 4, image))