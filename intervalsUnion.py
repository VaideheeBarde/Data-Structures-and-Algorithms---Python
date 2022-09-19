import collections

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))

def union_of_intervals(intervals):
    #Empty input
    if not intervals:
        return []

    #Sort intervals according to left endpoints of intervals
    intervals.sort(key = lambda i: (i.left.val, not i.left.is_closed))
    result = [intervals[0]]
    for i in intervals:
        if intervals and (i.left.val < result[-1].right.val or (i.left.val == result[-1].right.val and (i.left.is_closed or result[-1].right.is_closed))):
            if (i.right.val > result[-1].right.val or (i.right.val == result[-1].right.val and i.right.is_closed)):
                result[-1] = Interval(result[-1].left, i.right)
        else:
            result.append(i)
    
    return result

i1 = Interval(0,3)
epi11 = Endpoint(0,i1.left)
epi12 = Endpoint(0,i1.right)

i2 = Interval(1,1)
epi21 = Endpoint(1,i2.left)
epi22 = Endpoint(1,i2.right)

i3 = Interval(2,4)
epi31 = Endpoint(1,i3.left)
epi32 = Endpoint(1,i3.right)

i4 = Interval(3,4)
epi41 = Endpoint(1,i4.left)
epi42 = Endpoint(0,i4.right)

i5 = Interval(5,7)
epi51 = Endpoint(1,i5.left)
epi52 = Endpoint(0,i5.right)

i6 = Interval(7,8)
epi61 = Endpoint(1,i6.left)
epi62 = Endpoint(0,i6.right)

i7 = Interval(8,11)
epi71 = Endpoint(1,i7.left)
epi72 = Endpoint(0,i7.right)

i8 = Interval(9,11)
epi81 = Endpoint(0,i8.left)
epi82 = Endpoint(1,i8.right)

i9 = Interval(12,14)
epi91 = Endpoint(1,i9.left)
epi92 = Endpoint(1,i9.right)

i10 = Interval(12,16)
epi101 = Endpoint(0,i10.left)
epi102 = Endpoint(1,i10.right)

i11 = Interval(13,15)
epi111 = Endpoint(0,i11.left)
epi112 = Endpoint(0,i11.right)

i12 = Interval(16,17)
epi121 = Endpoint(0,i12.left)
epi122 = Endpoint(0,i12.right)

I = list()
I.append(i1)
I.append(epi11)
I.append(epi12)

I.append(i2)
I.append(epi21)
I.append(epi22)

I.append(i3)
I.append(epi31)
I.append(epi32)

I.append(i4)
I.append(epi41)
I.append(epi42)

I.append(i5)
I.append(epi51)
I.append(epi52)

I.append(i6)
I.append(epi61)
I.append(epi62)

I.append(i7)
I.append(epi71)
I.append(epi72)

I.append(i8)
I.append(epi81)
I.append(epi82)

I.append(i9)
I.append(epi91)
I.append(epi92)
print(I)

print(union_of_intervals(I))