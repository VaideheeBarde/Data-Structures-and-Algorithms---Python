#deep copy

import copy
li1 = [1,2,[3,5],4]
li2 = copy.deepcopy(li1)

print("original li1", li1)

li2[2][1] = 7

print("li1:", li1)
print("li2:", li2)

#shallow copy

import copy
li1 = [1,2,[3,5],4]
li2 = copy.copy(li1)

print("original li1", li1)

li2[2][1] = 7

print("li1:", li1)
print("li2:", li2)