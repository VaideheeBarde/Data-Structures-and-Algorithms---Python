Student = {"name": "Ankit", "age": 21, "sex": "Male", "college": "MNNIT Allahabad", "address": "Allahabad"} 
key = frozenset(Student) 
hashkey = hash(key)
print('The frozen set is:', key) 
print('The hash set is:', hashkey)