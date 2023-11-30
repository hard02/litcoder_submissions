def min_time_to_complete_tasks(tasks, workers):
    def is_valid(mid):
        current_workers = 1
        current_time = 0

        for task in tasks:
            current_time += task
            if current_time > mid:
                current_workers += 1
                current_time = task

        return current_workers <= workers

    low, high = max(tasks), sum(tasks)

    while low < high:
        mid = low + (high - low) // 2

        if is_valid(mid):
            high = mid
        else:
            low = mid + 1

    return low

# Input
num_tasks = int(input())
tasks_duration = list(map(int, input().split()))
num_workers = int(input())

# Output
result = min_time_to_complete_tasks(tasks_duration, num_workers)
print(result)

