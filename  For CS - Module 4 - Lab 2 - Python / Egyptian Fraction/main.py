def egyptian_fraction(numerator, denominator):
    result = []

    while numerator != 0:
        unit_fraction_denominator = -(-denominator // numerator)  # Ceiling division
        result.append(unit_fraction_denominator)

        numerator = numerator * unit_fraction_denominator - denominator
        denominator = denominator * unit_fraction_denominator

    return result

# Input reading
numerator = int(input().strip())
denominator = int(input().strip())

# Calculate and output the result
result = egyptian_fraction(numerator, denominator)
for fraction in result:
    print(fraction)
