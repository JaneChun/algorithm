from bisect import bisect_left

def solution(info, query):
    answer = []
    
    dict = {}
    
    for info_str in info:
        lang, pos, career, food, score = info_str.split(' ')
        
        options = [lang, pos, career, food]
        score = int(score)
        
        keys = []
        
        def dfs(idx, arr):
            if idx == 4:
                keys.append(' '.join(arr))
                return

            dfs(idx + 1, arr + [options[idx]]) # 실제 값
            dfs(idx + 1, arr + ['-'])          # '-' 값
        
        dfs(0, [])
        
        
        # dfs 종료 후 해당 key를 키로, score를 값으로 딕셔너리에 저장
        for key in keys:
            if key not in dict:
                dict[key] = [] # 같은 키가 여러명일 수 있으므로 배열로 처리
            dict[key].append(score)
            
    for key in dict:
        dict[key].sort()

    for q in query:
        arr = q.split(' and ')
        food, score = arr[3].split(' ')

        lang, pos, career = arr[0], arr[1], arr[2]
        score = int(score)
        
        query_key = ' '.join([lang, pos, career, food])
        
        scores = dict.get(query_key, [])

        idx = bisect_left(scores, score) # idx: score 이상인 값이 시작하는 인덱스
        count = len(scores) - idx # score 이상인 요소의 개수
        answer.append(count)
    
    return answer