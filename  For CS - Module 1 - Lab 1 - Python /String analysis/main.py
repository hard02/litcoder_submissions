def analyze_email_address(email):
    total_chars = len(email)
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    symbol_count = 0

    for char in email:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1

    uppercase_percentage = (uppercase_count / total_chars) * 100
    lowercase_percentage = (lowercase_count / total_chars) * 100
    digit_percentage = (digit_count / total_chars) * 100
    symbol_percentage = (symbol_count / total_chars) * 100

    print(f"{uppercase_percentage:.3f}%")
    print(f"{lowercase_percentage:.3f}%")
    print(f"{digit_percentage:.3f}%")
    print(f"{symbol_percentage:.3f}%")

# Example usage
email_address = input()
analyze_email_address(email_address)
                                                                                                                            
