def shortest_equivalent_path(path):
    if not path:
        raise ValueError("Empty string is not a valid path")

    path_names = [] #Uses list as a stack

    #Special case: starts with '/' which is an absolute path

    if path[0] == '/':
        path_names.append('/')

    for token in (token for token in path.split('/') if token not in ['.', '']):
        if token == '..':
            if not path_names or path_names[-1] == '..':
                path_names.append(token)
            else:
                if path_names[-1] == '/':
                    raise ValueError('Path Error')
                path_names.pop()
        else: #Must be a name
            path_names.append(token)

    result = '/'.join(path_names)
    return result[result.startswith('//'):]

print(shortest_equivalent_path('/usr/lib/bin/gcp/dev/java//.././/code/'))
print(shortest_equivalent_path("sc//./../tc/awk/././"))
print(shortest_equivalent_path("../usr/"))