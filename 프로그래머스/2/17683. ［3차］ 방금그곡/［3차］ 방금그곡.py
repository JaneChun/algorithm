from datetime import datetime

def solution(m, musicinfos):
    all_played = []
    m = replace_sharp(m) # 샵 처리
    
    for music_info in musicinfos:
        start, end, title, info = music_info.split(',')
        playtime = get_playtime(start, end)
        
        info = replace_sharp(info) # 샵 처리
        # played = ''.join([info[i % len(info)] for i in range(playtime)]) -> 시간이 클 경우 메모리, 시간 낭비
        played = (info * ((playtime // len(info)) + 1))[:playtime]
        
        if m in played:
            all_played.append([title, playtime])
    # print(all_played)
    
    if len(all_played) == 0:
        return '(None)'
            
    return sorted(all_played, key=lambda x: (-x[1]))[0][0]

def get_playtime(start, end):
    return convert_to_min(end) - convert_to_min(start)
    
def convert_to_min(hhmm):
    h, m = hhmm.split(':')
    return int(h) * 60 + int(m)

def replace_sharp(string):
    sharp_dict = {
        'C#': 'c',
        'D#': 'd',
        'E#': 'e',
        'F#': 'f',
        'G#': 'g',
        'A#': 'a',
        'B#': 'b'
    }
    
    for old, new  in sharp_dict.items():
        string = string.replace(old, new)  
    
    return string