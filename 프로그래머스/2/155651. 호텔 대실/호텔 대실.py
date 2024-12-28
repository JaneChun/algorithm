def solution(book_time):
    answer = 0
    rooms = [0] # 예약 가능 시간
    book_time_converted = convert_to_min(book_time)
    book_time_sorted = sorted(book_time_converted, key=lambda x: x[0])
        
    print(book_time_sorted)
    # [[900, 1030], [1000, 1110], [860, 930], [850, 1170], [1100, 1290]]
    
    for start,end in book_time_sorted:
        earliest_available = rooms[0]
        if earliest_available <= start:
            rooms[0] = end
        else:
            rooms.append(end)
            
        
        rooms.sort()
    
    print(rooms)
    return len(rooms)

def convert_to_min(book_time):
    result = []
    
    for start, end in book_time:
        [s_hour, s_min] = start.split(':')
        [e_hour, e_min] = end.split(':')
        start_converted = int(s_hour) * 60 + int(s_min)
        end_converted = int(e_hour) * 60 + int(e_min) + 10
        result.append([start_converted, end_converted])
        
    return result
        
    