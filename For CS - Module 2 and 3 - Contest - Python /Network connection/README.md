## Number of Operations to Make Network Connected
## Problem Statement
# Connecting a network

In a geographical region, there are N cities labeled from 1 to N. These cities are interconnected using various transportation routes forming a network. The city connectivity is represented by a list of connections between cities in the form of a 2D array route[][]. Each row (city1, city2) denotes a direct transportation route between city1 and city2.

Your task is to ensure that all cities are connected either directly or indirectly. To achieve this, you can perform the following operations:

    Remove any existing transportation route between two cities.
    Add a new transportation route between two disconnected cities.

Your goal is to find the minimum number of operations required to achieve full connectivity of all cities in the region.

Return the minimum number of times you need to do this in order to make all the cities connected. If it is not possible, return -1.

Example
Input: N = 6,

routes[][] = {{1, 2}, {2, 3}, {3, 5}, {4, 5}, {5, 6}}

Output:
1

Exercise-1

Input : 

6

5

0 1

0 2

0 3

1 2

1 3

Note:
Line 1: Available cities
Line 2 : No of routes
From line 3 : connected cities pair

Output :

2

Exercise-2

Input:

5

5

0 1

0 2

0 3

1 2

2 3


Output:

1

