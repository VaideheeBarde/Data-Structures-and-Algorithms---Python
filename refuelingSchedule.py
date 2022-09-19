import collections

MPG = 20

#gallons[i] is the amount of gas in  city i, and distance[i] is the distance city i to the next city
def find_ample_city(gallons, distances):
    remaining_gallons = 0
    CityAndRemainingGas = collections.namedtuple('CityAndRemainingGas', ('city', 'remaining_gallons'))
    city_remaining_gallons_pair = CityAndRemainingGas(0, 0)
    num_cities = len(gallons)

    for i in range(1, num_cities):
        remaining_gallons += gallons[i - 1] - distances[i - 1] // MPG
        if remaining_gallons < city_remaining_gallons_pair.remaining_gallons:
            city_remaining_gallons_pair = CityAndRemainingGas(i, remaining_gallons)
    
    return city_remaining_gallons_pair.city

gallons = [50,20,5,30,25,10,10]
distance = [900,600,200,400,600,200,100]

print(find_ample_city(gallons, distance))