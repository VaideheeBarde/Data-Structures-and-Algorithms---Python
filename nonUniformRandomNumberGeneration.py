import random
import bisect
import itertools

def nonuniform_random_number_generation(values, probabilities):
    prefixSumOfProbabilities = list(itertools.accumulate(probabilities))
    intervalIndex = bisect.bisect(prefixSumOfProbabilities, random.random())
    return values[intervalIndex]

print(nonuniform_random_number_generation([1,2,7,9],[(1/18),(2/18),(3/18),(7/18)]))