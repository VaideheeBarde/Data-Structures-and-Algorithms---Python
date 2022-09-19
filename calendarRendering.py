import collections

#Event is a tuple(start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

#Endpoint is a tuple(start_time, 0) or (end_time, 1) so that if times are equal, start_time comes first
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))

def find_max_simultaneous_events(A):
    #Builds an array of all endpoints
    E = [p for event in A for p in (Endpoint(event.start, True), Endpoint(event.finish, False))]

    #Sorts the endpoint array according to the time, breaking ties by putting start times before end times
    E.sort(key=lambda e: (e.time, not e.is_start))

    #Track the number of simultaneous events, record the maximum number of simultaneous events
    max_num_simultaneous_events, num_simultaneous_events = 0, 0

    for e in E:
        if e.is_start:
            num_simultaneous_events += 1
            max_num_simultaneous_events = max(num_simultaneous_events, max_num_simultaneous_events)
        else:
            num_simultaneous_events -= 1

    return max_num_simultaneous_events

e1 = Event(1,5)
e2 = Event(6,10)
e3 = Event(11,13)
e4 = Event(14,15)
e5 = Event(2,7)
e6 = Event(8,9)
e7 = Event(12,15)
e8 = Event(4,5)
e9 = Event(9,17)

ep1s = Endpoint(1,0)
ep1e = Endpoint(5,1)
ep2s = Endpoint(6,0)
ep2e = Endpoint(10,1)
ep3s = Endpoint(11,0)
ep3e = Endpoint(13,1)
ep4s = Endpoint(14,0)
ep4e = Endpoint(15,1)
ep5s = Endpoint(2,0)
ep5e = Endpoint(7,1)
ep6s = Endpoint(8,0)
ep6e = Endpoint(9,1)
ep7s = Endpoint(12,0)
ep7e = Endpoint(15,1)
ep8s = Endpoint(4,0)
ep8e = Endpoint(5,1)
ep9s = Endpoint(9,0)
ep9e = Endpoint(17,1)

A = list()
A.append(e1)
A.append(e2)
A.append(e3)
A.append(e4)
A.append(e5)
A.append(e6)
A.append(e7)
A.append(e8)
A.append(e9)

print(find_max_simultaneous_events(A))