import timeit
import functools

def time_function(f):
    begin = timeit.default_timer()
    result = f()
    end = timeit.default_timer()
    print('Function call took ' + str(end - begin) + ' seconds to execute')
    return result

def foo():
    print('I am foo')

def ackermann(m,n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

time_function(foo)
#functools.partial() take a function and positional arguments to it and
#creates a new function with those arguments preassigned to the specified values
time_function(functools.partial(ackermann, 3, 4))