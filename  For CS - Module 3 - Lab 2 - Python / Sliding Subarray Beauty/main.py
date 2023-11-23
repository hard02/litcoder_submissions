def sliding_subarray_beauty(arr, k, n):
    result = []
    for i in range(len(arr) - k + 1):
        subarray = arr[i:i + k]
        sorted_subarray = sorted(subarray)
        result.append(sorted_subarray[n - 1])
    return result

# Input reading
arr = list(map(int, input().strip().split()))
k = int(input().strip())
n = int(input().strip())

# Calculate and output the result
result = sliding_subarray_beauty(arr, k, n)
print(*result)
                                                                                                                            
