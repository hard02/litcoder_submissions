def mix_the_array(n, q, queries):
    array = [0] * n

    for query in queries:
        start, end, value = query
        array[start - 1] += value
        if end < n:
            array[end] -= value

    max_value = array[0]
    current_value = array[0]

    for i in range(1, n):
        current_value += array[i]
        max_value = max(max_value, current_value)

    return max_value

# Input reading
n = int(input().strip())
q = int(input().strip())

queries = []
for _ in range(q):
    query = list(map(int, input().strip().split()))
    queries.append(query)

# Calculate and output the result
result = mix_the_array(n, q, queries)
print(result)
                                                                                                                            
