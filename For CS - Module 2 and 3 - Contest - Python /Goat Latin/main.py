def toGoatLatin(S):
    vowels = set('aeiouAEIOU')
    words = S.split()
    result = []
    
    for i, word in enumerate(words, 1):
        if word[0] in vowels:
            word += 'ma' + 'a' * i
        else:
            word = word[1:] + word[0] + 'ma' + 'a' * i
        
        result.append(word)
    
    return ' '.join(result)
    
S = input()

print(toGoatLatin(S))
