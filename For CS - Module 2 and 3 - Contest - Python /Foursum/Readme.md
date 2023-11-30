Given an array nums of n integers, the task is to find all unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that the sum of the elements at indices a, b, c, and d is equal to the given target.

The quadruplets must satisfy the following conditions:

All indices a, b, c, and d should be within the range 0 to n-1.
Indices a, b, c, and d must be distinct (no repeated indices).
The sum of nums[a], nums[b], nums[c], and nums[d] should be equal to the target.

Return the array of all unique quadruplets that meet these conditions. The order of the quadruplets in the output array does not matter.


Example 1:

Input: nums = [4, 5, 3, 2, 9, 1], target = 12

Output: [[9, 2, 1, 0], [5, 4, 2, 1], [9, 3, 2, -2]]

Example 2:

Input: nums = [-3, 1, -5, 7, 0, -2], target = -1

Output: [[7, -3, -2, -5], [0, 1, -3, -1], [-2, 1, 0, -5]]

The function should find all unique quadruplets in the nums array, where each quadruplet's elements sum to the given target. The quadruplets should satisfy the specified conditions and can be returned in any order. The examples provided use different number values to illustrate the problem.

Exercise-1

Input : 
1 0 -1 0 -2 2
1

Output :
-2 0 1 2
-1 0 0 2
