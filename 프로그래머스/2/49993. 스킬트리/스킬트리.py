def solution(skill, skill_trees):
    count = 0
    skill_order = {}
    
    for i, s in enumerate(skill):
        skill_order[s] = i
    
    for skill_tree in skill_trees:
        is_possible = True
        filtered_skill_tree = list(filter(lambda x: x in skill, skill_tree))
        
        for i in range(len(filtered_skill_tree)):
            cur_skill = filtered_skill_tree[i]
            if cur_skill != skill[i]: # filtered_skill_tree의 순서가 skill의 순서를 따라야 함
                is_possible = False
                break
        
        if is_possible:
            count += 1 
    
    return count