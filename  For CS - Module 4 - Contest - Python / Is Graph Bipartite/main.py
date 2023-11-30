
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(node, c):
            color[node] = c
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    if not dfs(neighbor, 1 - c):
                        return False
                elif color[neighbor] == c:
                    return False
            return True

        for i in range(n):
            if color[i] == -1 and not dfs(i, 0):
                return False

        return True

# Input
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# Output
solution = Solution()
output = solution.isBipartite(graph)
print(output)
