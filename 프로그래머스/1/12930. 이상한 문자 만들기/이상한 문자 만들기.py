def solution(s):
    result = []
    for word in s.split(' '):
        converted_word = ''
        for i, char in enumerate(word):
            if i % 2 == 0:
                converted_word += char.upper() 
            else: 
                converted_word += char.lower()
        result.append(converted_word)
    return ' '.join(result)
            