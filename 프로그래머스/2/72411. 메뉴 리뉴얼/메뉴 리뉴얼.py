def solution(orders, course):
    answer = []
    combo_count = dict()
    
    for length in course:
        combo_count[length] = dict()
        
        for order in orders:
            combos = []
            
            sorted_order = sorted(list(order))
            dfs(sorted_order, [], length, 0, combos)
            
            for combo in combos:
                combo = ''.join(combo)
                combo_count[length][combo] = combo_count[length].get(combo, 0) + 1
    
    # print(combo_count)
    
    for length, combos in combo_count.items():
        if len(combos) == 0:
            continue
            
        max_count = max(combos.values())
        
        top_combos = [combo for combo, count in combos.items() if count == max_count and count >= 2]
        # print(top_combos)
        
        answer.extend(top_combos)
            
        
    return sorted(answer)

def dfs(menu_items, current_combo, length, start, result):
    if len(current_combo) == length:
        result.append(current_combo[:])
        return
    
    for i in range(start, len(menu_items)):
        current_combo.append(menu_items[i])
        dfs(menu_items, current_combo, length, i + 1, result) # DFS
        current_combo.pop() # 백트래킹