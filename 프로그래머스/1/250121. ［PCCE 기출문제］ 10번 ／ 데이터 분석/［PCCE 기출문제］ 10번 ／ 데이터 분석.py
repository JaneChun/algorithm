def solution(data, ext, val_ext, sort_by):
    answer = []
    
    key = ['code', 'date', 'maximum', 'remain']
    mapped_data = [dict(zip(key, value)) for value in data]
    # [{code:, date: , }, {...}]
    
    for obj in mapped_data:
        if ext == 'date':
            if str(obj.get(ext)) < str(val_ext):
                answer.append(obj)
        elif obj.get(ext) < val_ext:
            answer.append(obj)
        
    sorted_answer = sorted(answer, key=lambda x:  x.get(sort_by))
            
    return [[obj['code'], obj['date'], obj['maximum'], obj['remain']] for obj in sorted_answer]