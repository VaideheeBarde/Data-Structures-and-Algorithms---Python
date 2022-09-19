class ContactList:
    def __init__(self, names):
        '''
        names is a list of strings
        '''
        self.names = names

    def __hash__(self):
        #Conceptually we want to hash the set of names
        #Since the set type is mutable, it cannot be hashed. Therefore we use frozenset
        return hash(frozenset(self.names))

    def __eq__(self, other):
        return set(self.names) == set(other.names)

def merge_contact_lists(contacts):
    return list(set(contacts))

c1 = ContactList("Jim")
c2 = ContactList("Pam")
c3 = ContactList("Dwight")
c4 = ContactList("Angela")
c5 = ContactList("Michael")

contacts = []

contacts.append(c1)
contacts.append(c2)
contacts.append(c3)
contacts.append(c4)
contacts.append(c5)

print(merge_contact_lists(contacts))