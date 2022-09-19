import random 
import itertools

def online_sampling(stream, k):
    running_sample = list(itertools.islice(stream, k))
    number_seen_so_far = k

    for x in stream:
        number_seen_so_far += 1
        index_to_replace = random.randrange(number_seen_so_far)

        if index_to_replace < k:
            running_sample[index_to_replace] = x

    return running_sample

print(online_sampling([12,29,23,64,51],2))
print(online_sampling([12,29,23,64,51],4))