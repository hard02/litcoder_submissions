
Problem Statement
Job Sequencing

The problem at hand involves a set of jobs, each with a deadline and an associated profit. These jobs are subject to the constraint that only one job can be scheduled at a time, and each job takes exactly one unit of time to complete. The minimum deadline for a job is 1.
Input: The input consists of an array of jobs with their respective deadlines and profits. The order in which the jobs are listed in the input does not necessarily represent the optimal order.

Job - Deadline - Profit
A   -       2 -        100
C      -    2         -   27
D        -  1  -          25
E     -      3    -        15
B     -     1       -     19

The goal is to find a sequence of jobs that maximizes the total profit, subject to the constraint that each job must be completed before its deadline.

Important Note: Ensure that you save your solution before progressing to the next question and  before submitting your answer.

Exercise-1

Input:
6
a b c d e
2 1 2 1 3
100 19 27 25 15

Note:
Line 1: job count
Line 2: job name
Line 3: deadline
Line 4:Profit

Output:

c a e

Exercise-2

Input:

5
p q r s t
2 1 3 1 3
99 190 27 25 15

Output:
q p r
