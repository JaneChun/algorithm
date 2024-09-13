def solution(n, words):
    answer = [0, 0]
    said_words = set()
    
    for i in range(0, len(words)):
        if i == 0:
            said_words.add(words[i])
            continue
        
        prev_word = words[i - 1]
        cur_word = words[i]
        
        # 게임 종료 조건 : 끝말이 틀린경우 or 중복 단어 말한 경우
        if prev_word[-1] != cur_word[0] or cur_word in said_words:
            game_round = (i // n) + 1
            cur_person = (i % n) + 1
            return [cur_person, game_round]
        
        said_words.add(cur_word)
        
    return answer