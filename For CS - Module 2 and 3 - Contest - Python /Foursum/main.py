def fourSum(nums, target):
    nums.sort()
    result = []

    for i in range(len(nums) - 3):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 2):
            # Skip duplicate values for the second element
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left, right = j + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    # Skip duplicate values for the third element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicate values for the fourth element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return result

# Input
nums = list(map(int, input().split()))
target = int(input())

# Output
result = fourSum(nums, target)
for quad in result:
    print(" ".join(map(str, quad)))

