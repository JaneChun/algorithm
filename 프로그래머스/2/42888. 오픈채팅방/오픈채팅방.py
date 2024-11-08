def solution(record):
    answer = []
    uid_name_dict = {}
    
    for r in record:
        inputs = r.split(' ')
        action, uid = inputs[0], inputs[1]
        
        if action in ('Enter', 'Change'):
            name = inputs[2]
            uid_name_dict[uid] = name
            
        if action in ('Enter', 'Leave'):
            answer.append([action, uid])
            
    result = []
    
    for [action, uid] in answer:
        name = uid_name_dict[uid]
        
        if action == 'Enter':
            result.append(f"{name}님이 들어왔습니다.")
        else:
            result.append(f"{name}님이 나갔습니다.")
    
    return result