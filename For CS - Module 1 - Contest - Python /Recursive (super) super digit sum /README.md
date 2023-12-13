 Recursive (Super) Digit Sum
Problem Statement
Find the super digit of a repeating number

Let's consider the scenario of Alice and Bob. Alice has the number 987 and Bob wants to find the super digit of this number repeated 5 times. The super digit follows the following rules:

If a number has only one digit, its super digit is equal to that digit.
Otherwise, the super digit of a number is calculated as the super digit of the sum of its digits.
In this case, Alice's number is 987, and Bob wants to repeat it 5 times. So, n = 987 and k = 5. Thus, n k is equal to 987987987987987. To find the super digit, we calculate the sum of the digits: (9 + 8 + 7 + 9 + 8 + 7 + 9 + 8 + 7 + 9 + 8 + 7 + 9 + 8 + 7 + 9 + 8 + 7) = 153. Since 153 has three digits, we further calculate its super digit: (1 + 5 + 3) = 9. Therefore, the super digit of 987 repeated 5 times is 9.

Important Note: Ensure that you save your solution before progressing to the next question and  before submitting your answer.

Exercise-1
input:
56785
2
output:
8

Exercise-2
input:
65109
3
Output:
9
