import collections

Person = collections.namedtuple('Person', ('age', 'name'))

def group_by_age(people):
    age_to_count = collections.Counter(person.age for person in people)

    age_to_offset, offset = {}, 0

    for age, count in age_to_count.items():
        age_to_offset[age] = offset
        offset += count

    while age_to_offset:
        from_age = next(iter(age_to_offset))
        from_idx = age_to_offset[from_age]
        to_age = people[from_idx].age
        to_idx = age_to_offset[people[from_idx].age]
        people[from_idx], people[to_idx] = people[to_idx], people[from_idx]
        #Use age to count to see when we are finished with a particular age
        age_to_count[to_age] -= 1
        if age_to_count[to_age]:
            age_to_offset[to_age] = to_idx + 1
        else:
            del age_to_offset[to_age]


people = []

p1 = Person(14, 'Greg')
p2 = Person(12, 'John')
p3 = Person(11, 'Andy')
p4 = Person(13, 'Jim')
p5 = Person(12, 'Phil')
p6 = Person(13, 'Bob')
p7 = Person(13, 'Chip')
p8 = Person(14, 'Tim')

people.append(p1)
people.append(p2)
people.append(p3)
people.append(p4)
people.append(p5)
people.append(p6)
people.append(p7)
people.append(p8)

print(people)
group_by_age(people)
print(people)