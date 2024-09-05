def solution(s):
    answer = []
    
    for word in s.split(' '):
        if word == '': # 빈 문자열 유지            
            answer.append(word)
        else:
            if (word[0]).isdigit():
                answer.append(word.lower())
            else:
                new_word = word[0].upper() + word[1:].lower()
                answer.append(new_word)
    return ' '.join(answer)