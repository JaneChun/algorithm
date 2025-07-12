from collections import defaultdict

# 장르 별로 가장 많이 재생된 노래 2개씩 리턴
# { classic: {
#       total_plays: 1450,
#       songs: [ {number: 0, plays: 500 }, ... ]
#   }, 
#   ... 
# }
    
def solution(genres, plays):
    answer = []
    genre_map = defaultdict(lambda: {'total_plays': 0, 'songs': []})
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_map[genre]['total_plays'] += play
        genre_map[genre]['songs'].append({'number': i, 'play': play})
    
    sorted_genres = sorted(genre_map.values(), key=lambda x: -x['total_plays'])
    
    for genre in sorted_genres:
        top_2_songs = sorted(genre['songs'], key=lambda x: (-x['play'], x['number']))[:2]
        answer.extend([song['number'] for song in top_2_songs])
    
    return answer