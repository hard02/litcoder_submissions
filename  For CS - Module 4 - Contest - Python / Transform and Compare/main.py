def canTransform(start: str, end: str) -> bool:
    if len(start) != len(end):
        return False

    i, j = 0, 0
    while i < len(start) and j < len(end):
        while i < len(start) and start[i] == 'X':
            i += 1
        while j < len(end) and end[j] == 'X':
            j += 1

        if (i == len(start)) != (j == len(end)):
            return False

        if i < len(start) and j < len(end):
            if start[i] != end[j] or (start[i] == 'L' and i < j) or (start[i] == 'R' and i > j):
                return False

        i += 1
        j += 1

    return True


start = input()
end = input()

# Output
output = canTransform(start, end)
print(output)
                                                                                                                            
