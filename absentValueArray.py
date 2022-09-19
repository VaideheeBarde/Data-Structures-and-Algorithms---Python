import itertools

def find_missing_element(stream):
    num_bucket = 1 << 16
    counter = [0] * num_bucket
    stream, stream_copy = itertools.tee(stream)

    for x in stream:
        upper_part_x = x >> 16
        counter[upper_part_x] += 1

    #Look for a bucket that contains less than (1<<16) elements
    bucket_capacity = 1 << 16
    candidate_bucket = next(i for i, c in enumerate(counter) if c < bucket_capacity)

    #Find all IP addresses in the stream whose first 16 bits are equal to candidate bucket
    candidates = [0] * bucket_capacity
    stream = stream_copy
    for x in stream_copy:
        upper_part_x = x >> 16
        if candidate_bucket == upper_part_x:
            #Record the presence of 16 LSB of x
            lower_part_x = ((1<<16) - 1) & x
            candidates[lower_part_x] = 1

    #At least one of the LSB combinations is absent, find it.
    for i, v in enumerate(candidates):
        if v == 0:
            return (candidate_bucket << 16) | i

print(find_missing_element([0,1,2,3,5]))
print(find_missing_element([1,3,4,5,7]))