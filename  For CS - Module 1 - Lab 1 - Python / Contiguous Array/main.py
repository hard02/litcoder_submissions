def findMaxLength(nums):
    nums = list(map(int, nums.split()))

    
    sum_index_map = {0: -1}
    max_length = 0
    current_sum = 0

    for index, num in enumerate(nums):
        
        current_sum += 1 if num == 1 else -1
        
        if current_sum in sum_index_map:
            max_length = max(max_length, index - sum_index_map[current_sum])
        else:
            sum_index_map[current_sum] = index

    return max_length
    
    
nums=input()
print(findMaxLength(nums))
