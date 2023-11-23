
Problem Statement
Maximize Subsequences in String
You are given two strings, **text** and **pattern**, both consisting of only lowercase English letters. The objective is to modify the text by adding either pattern[0] or pattern[1] exactly once at any position. After the modification, you need to determine the maximum number of times the pattern can occur as a subsequence in the modified text.

A subsequence is a sequence of characters obtained by deleting some or no characters from the original sequence without changing the order of the remaining characters.
Important Note:

Ensure that you save your solution before progressing to the next question and  before submitting your answer.
Example with Explanation

Input text is “abdcdbc”.  Input Pattern is “ac”.
When inserting 'a' as Pattern [0] between text [1] and text [2], the resulting string is "abadcdbc." After deleting “bd” in the newly created text, we will get “aacc”. In this modified string, the subsequence "ac" appears four times.

Some other combinations are,
aabdcdbc  -> aacc -> Four times
abdacdbc -> aacc-> Four times
abdcadbc -> acac -> Three times
abdccdbc -> accc -> Three times
abdcdbcc -> accc -> Three times

Input and Output format:

Exercise-1


Input: 
 
ababc
ab

Output:
5


Exercise-2


Input: 
 
ababab
ab

Output:
9


