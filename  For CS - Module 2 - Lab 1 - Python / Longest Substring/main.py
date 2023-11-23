def longest_substring_length(s):
    char_index_map = {}
    start = 0
    max_length = 0

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1

        char_index_map[char] = i
        current_length = i - start + 1
        max_length = max(max_length, current_length)

    return max_length
    
    
input_str = input()

output = longest_substring_length(input_str)
print(f"{output}")
                                                                                                                            
