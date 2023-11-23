def clumsy(n):
    if n <= 2:
        return n

    stack = [n]
    n -= 1
    operations = ['*', '//', '+', '-']
    op_index = 0

    while n > 0:
        if operations[op_index] == '*':
            stack[-1] *= n
        elif operations[op_index] == '//':
            stack[-1] //= n
        elif operations[op_index] == '+':
            stack.append(n)
        else:
            stack.append(-n)

        n -= 1
        op_index = (op_index + 1) % 4

    return sum(stack)
    
# Input reading
n = int(input().strip())

# Calculate and output the clumsy factorial
result = clumsy(n)
print(result)
                                                                                                                            
