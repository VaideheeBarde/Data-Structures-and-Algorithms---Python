def snakeString(s):
    return s[1::4] + s[0::2] + s[3::4]

print(snakeString("Hello_World"))