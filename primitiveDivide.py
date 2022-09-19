def divide(x, y):
    result = 0
    power = 32

    y_power = y<<power

    while x>=y:
        while y_power>x:
            y_power>>=1
            power-=1
        result+=1<<power
        x-=y_power

    return result

print(divide(18,3))