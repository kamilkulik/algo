def min_waiting_time(queries):
    queries.sort()
    wait_times = [0]
    for idx in range(1, len(queries)):
        wait_time = wait_times[idx - 1] + queries[idx -1]
        wait_times.append(wait_time)
    return sum(wait_times)

def min_waiting_time_smart(queries):
    # 1. sort input array - we want to have biggest wait time at the end
    queries.sort()
    # 2. initialise variable to hold the wait time
    wait_sum = 0
    # 3. loop over the queries
    for idx in range(len(queries)):
        # 4. multiply current waiting time by the number of times subsequent items will need to wait for it
        waiting_time = queries[idx] * (len(queries) - 1 - idx)
        # 5. increment wait_sum by waiting_time
        wait_sum += waiting_time
    return wait_sum
