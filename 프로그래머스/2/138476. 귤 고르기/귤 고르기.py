def solution(k, tangerine):
    count_dict = {}
    for size in tangerine:
        if not count_dict.get(size):
            count_dict[size] = 0
        count_dict[size] += 1
    
    sorted_by_count = sorted(count_dict.items(), key = lambda item: item[1], reverse=True)
   
    type_count = 0
    box = 0
    for size, count in sorted_by_count:
        box += count
        type_count += 1
        if box >= k:
            return type_count