import collections
import operator

Interval = collections.namedtuple('Interval', ('left', 'right'))

def find_minimum_visits(intervals):
    #Sort intervals based on the right endpoints
    intervals.sort(key = operator.attrgetter('right'))
    last_visit_time, num_visits = float('-inf'), 0

    for interval in intervals:
        if interval.left > last_visit_time:
            #The current right endpoint, last_visit_time, will not cover any more intervals
            last_visit_time = interval.right
            num_visits += 1

    return num_visits

intervals = []

interval1 = Interval(1,2)
interval2 = Interval(2,3)
interval3 = Interval(3,4)
interval4 = Interval(2,3)
interval5 = Interval(3,4)
interval6 = Interval(4,5)
interval7 = Interval(5,6)

intervals.append(interval1)
intervals.append(interval2)
intervals.append(interval3)
intervals.append(interval4)
intervals.append(interval5)
intervals.append(interval6)
intervals.append(interval7)

print(find_minimum_visits(intervals))

#O(1) time per index
#time complexity after initial sort is O(n)