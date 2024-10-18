def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = [city.lower() for city in cities]
    
    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                if len(cache):
                    cache.pop(0)
                    cache.append(city)
            answer += 5
        
    return answer