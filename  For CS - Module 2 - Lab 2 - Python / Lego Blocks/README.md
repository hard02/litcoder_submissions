 Problem Statement
Build a wall with lego blocks

How many different ways can you build a wall of height 'n' and width 'm' using an infinite number of Lego bricks of four types, each with different dimensions (depth x height x width)? The types of Lego bricks available are:

Depth: 1, Height: 1, Width: 1
Depth: 1, Height: 1, Width: 2
Depth: 1, Height: 1, Width: 3
Depth: 1, Height: 1, Width: 4

The wall should satisfy the following conditions:

    There should be no holes in the wall.
    The wall should be a single solid structure without a straight vertical break across all rows of bricks.
    The bricks must be laid horizontally.

Provide the number of ways to build the wall, considering that the result should be output modulo 1000000007.

Example:

For n = 2 and m = 2, the output should be legoWall(n, m) = 3.
For n = 3 and m = 2, the output should be legoWall(n, m) = 7.
For n = 2 and m = 3, the output should be legoWall(n, m) = 9.

Input/Output:

1.The input consists of two integers: n and m, representing the desired height and width of the wall, respectively.
2.The output is a long integer representing the number of ways to build the wall, modulo 1000000007.

Exercise-1
Input:
2
2

Here
First row - n value
Second row - m value

Output:
3

Exercise-2
Input:
4
4
