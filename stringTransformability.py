import collections
import string

def transform_string(D, s, t):
    StringWithDistance = collections.namedtuple('StringWithDistance', ('candidate_string', 'distance'))
    q = collections.deque([StringWithDistance(s, 0)])
    D.remove(s)

    while q:
        f = q.popleft()
        #Returns if we find a match
        if f.candidate_string == t:
            return f.distance

        #Tries all possible transformations of f.candidate_string
        for i in range(len(f.candidate_string)):
            for c in string.ascii_lowercase:
                cand = f.candidate_string[:i] + c + f.candidate_string[i + 1:]
                if cand in D:
                    D.remove(cand)
                    q.append(StringWithDistance(cand, f.distance + 1))

    return -1  #Cannot find a possible transformations

D = {'bat', 'cot', 'dog', 'dag', 'dot', 'cat'}
s = 'cat'
t = 'dog'

print(transform_string(D, s, t))