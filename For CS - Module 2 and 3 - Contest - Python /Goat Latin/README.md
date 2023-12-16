## Problem Statement
# Goat Latin Conversion

Given a sentence, S, consisting of words separated by spaces, we want to convert it into "Goat Latin," which is a fictional language similar to Pig Latin.

The rules for Goat Latin conversion are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word. For example, the word 'apple' becomes 'applema'.

If a word begins with a consonant (a letter that is not a vowel), remove the first letter, append it to the end of the word, and then add "ma". For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word based on its word index in the sentence, starting with 1. For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.

Write a program that takes the sentence S as input and returns the final sentence representing its conversion into Goat Latin.

Important Note: Ensure that you save your solution before progressing to the next question and  before submitting your answer.

Exercise 1:

Input:
aasssdd

Output:
aasssddmaa
