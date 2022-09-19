
#Method 1
def foo(x, y, z):
    return x * x + y * y + z * z

print(foo(x=1,y=2,z=3))



#Method 2
def foo(x=[]):
    print(x)
    x.append(1)
    return x

result = foo()
print(result)
result = foo()
print(result)



######Read file as array######

#Method 1 - Buggy
def read_file_as_array_buggy(filename, default = []):
    try:
        filehandle = open(filename)
        return filename.read().split()
    except Exception:
        return default

#Method 2 - Works
def read_file_as_array_works(filename, default = None):
    if default is None:
        default = []
    try:
        filehandle = open(filename)
        return filename.read().split()
    except Exception:
        return default

A = read_file_as_array_buggy('does_not_exist.txt')
A.append('first')
print(A)
B  = read_file_as_array_buggy('does_not_exist.txt')
B.append('second')
print(B)

A = read_file_as_array_works('does_not_exist.txt')
A.append('first')
print(A)
B = read_file_as_array_works('does_not_exist.txt')
B.append('second')
print(B)