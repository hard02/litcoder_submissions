    def calculate_super_digit(number):
        if len(str(number)) == 1:
            return number
        else:
            return calculate_super_digit(sum(map(int, str(number))))

    super_digit = calculate_super_digit(n * k)
    return super_digit

n = int(input())
k = int(input())

super_digit_result = superDigit(n, k)
print(super_digit_result)
                                                                                                                                                                                                         
