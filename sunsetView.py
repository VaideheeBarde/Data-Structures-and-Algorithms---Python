import collections
from collections import namedtuple

def examine_buildings_with_sunset(sequence):
    BuildingWithHeight = collections.namedtuple('BuildingWithHeight', ('id', 'height'))
    candidates = []

    for building_idx, building_height in enumerate(sequence):
        while candidates and building_height >= candidates[-1].height:
            candidates.pop()
        candidates.append(BuildingWithHeight(building_idx, building_height))
    
    return [c.id for c in reversed(candidates)]

#sequence takes buildings from east-to-west
print(examine_buildings_with_sunset([1,2,3,4]))
print(examine_buildings_with_sunset([4,3,2,1]))