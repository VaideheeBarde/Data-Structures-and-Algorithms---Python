import collections

Interval = collections.namedtuple('Interval', ('left', 'right'))

def add_interval(disjoint_intervals, new_interval):
    i, result = 0, []

    #Processes intervals in disjoint_intervals which come before new interval
    while(i < len(disjoint_intervals) and new_interval.left > disjoint_intervals[i].right):
        result.append(disjoint_intervals[i])
        i += 1

    #Processes intervals in disjoint_intervals which overlap with new_interval
    while(i < len(disjoint_intervals) and new_interval.right >= disjoint_intervals[i].left):
        #If [a,b] and [c,d] overlap, union is [min(a,c), max(b,d)]
        new_interval = Interval(min(new_interval.left, disjoint_intervals[i].left), max(new_interval.right, disjoint_intervals[i].right))
        i += 1

    #Processes intervals in disjoint_intervals which come after new_interval
    return result + [new_interval] + disjoint_intervals[i:]

i1 = Interval(-4, -1)
i2 = Interval(0, 2)
i3 = Interval(3, 6)
i4 = Interval(7, 9)
i5 = Interval(11, 12)
i6 = Interval(14, 17)

I = list()
I.append(i1)
I.append(i2)
I.append(i3)
I.append(i4)
I.append(i5)
I.append(i6)

newI = Interval(1,8)

print(add_interval(I, newI))