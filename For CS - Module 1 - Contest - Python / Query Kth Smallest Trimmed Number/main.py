def kth_smallest_trimmed_number(nums, queries):
    answer = []

    for query in queries:
        position, trim_length = query
        trimmed_nums = []

        for num in nums:
            trimmed = int(num[-trim_length:] if len(num) >= trim_length else num)
            trimmed_nums.append(trimmed)

        sorted_nums = sorted(trimmed_nums)
        kth_smallest = sorted_nums[position - 1] if position <= len(sorted_nums) else -1
        kth_smallest_index = trimmed_nums.index(kth_smallest) if kth_smallest != -1 else -1
        answer.append(kth_smallest_index)

    return answer

# Input reading
nums = input().strip().split()
queries_count = int(input().strip())

queries = []
for _ in range(queries_count):
    query = list(map(int, input().strip().split()))
    queries.append(query)

# Calculate and output the result
result = kth_smallest_trimmed_number(nums, queries)
print(" ".join(map(str, result)))
                                                                                                                            
