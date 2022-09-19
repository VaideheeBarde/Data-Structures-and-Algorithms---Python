import random

def randomSubset(n, k):
    changedElements = {}

    for i in range(k):
        randomIndex = random.randrange(i,n)
        randomIndexMapped = changedElements.get(randomIndex, randomIndex)
        indexMapped = changedElements.get(i,i)

        changedElements[randomIndex] = indexMapped
        changedElements[i] = randomIndexMapped

    return [changedElements[i] for i in range(k)]

print(randomSubset(10, 3))
print(randomSubset(3, 3))