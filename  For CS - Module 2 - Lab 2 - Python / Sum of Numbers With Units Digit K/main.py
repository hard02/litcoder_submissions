def minimumNumbers( num: int, k: int) -> int:
    if num==0:
        return 0 
    if k==0:
        if num%10==0:
            return 1
        return -1
    if num<k:
        return -1 
    d = {
        1:[1,2,3,4,5,6,7,8,9,0],
        2:[2,4,6,8,0],
        3:[3,6,9,2,5,8,1,4,7,0],
        4:[4,8,2,6,0],
        5:[5,0],
        6:[6,2,8,4,0],
        7:[7,4,1,8,5,2,9,6,3,0],
        8:[8,6,4,2,0],
        9:[9,8,7,6,5,4,3,2,1,0]
    }
    if num%10 not in d[k]:
        return -1 
    else:
        i = d[k].index(num%10) + 1 
        if num<i*k:
            return -1 
        return i
# Example usage

num = int(input().strip())
try:
    k = int(input().strip())
except:
    k=0
result = minimumNumbers(num, k)
print(result)
                                                                                                                            
