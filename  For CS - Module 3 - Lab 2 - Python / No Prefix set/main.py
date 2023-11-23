def is_good_password(passwords):
    passwords.sort()
    for i in range(len(passwords) - 1):
        if passwords[i + 1].startswith(passwords[i]):
            return "BAD PASSWORD"
    return "GOOD PASSWORD"

# Input reading
passwords = input().strip().split()

# Check and output result
result = is_good_password(passwords)
print(result)
                                                                                                                            
