def solution(s):
    return ' '.join(
        map(lambda word: 
            ''.join(
                [char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(word)]
            )
        , s.split(' ')))


    # result = []
    # for word in s.split(' '):
    #     converted_word = ''
    #     for i, char in enumerate(word):
    #         if i % 2 == 0:
    #             converted_word += char.upper() 
    #         else: 
    #             converted_word += char.lower()
    #     result.append(converted_word)
    # return ' '.join(result)
            