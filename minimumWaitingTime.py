def minimum_total_waiting_time(service_times):
    #Sort the service times in increasing order
    service_times.sort()
    total_waiting_time = 0

    for i, service_time in enumerate(service_times):
        num_remaining_queries = len(service_times) - (i + 1)
        total_waiting_time += service_time * num_remaining_queries

    return total_waiting_time

print(minimum_total_waiting_time([2,5,1,3]))

#Time complexity = O(nlogn)