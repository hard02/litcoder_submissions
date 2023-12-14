def job_sequencing(job_count, jobs, deadlines, profits):
    arr = list(zip(jobs, deadlines, profits))
    arr.sort(key=lambda x: (-x[2], x[1]))

    result = [False] * max(deadlines)
    scheduled_jobs = ['-1'] * max(deadlines)

    for i in range(len(arr)):
        for j in range(min(max(deadlines) - 1, arr[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                scheduled_jobs[j] = arr[i][0]
                break

    return scheduled_jobs


# Reading input values
job_count = int(input())
jobs = input().split()
deadlines = list(map(int, input().split()))
profits = list(map(int, input().split()))

# Calling the function
scheduled_jobs = job_sequencing(job_count, jobs, deadlines, profits)

# Outputting the result
print(' '.join(scheduled_jobs))
