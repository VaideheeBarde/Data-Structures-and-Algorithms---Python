# >> operator is the same as dividing by 2//1

def power(x,y):
    result = 1.0
    power = y

    if power<0:
        power, x = -power, 1.0/x

    while power:
        if power & 1:
            result *= x
            
        x, power = x*x, power>>1

    return result

print(power(3,3))