def solution(cacheSize, cities):
    cache = []
    time = 0
    for city in cities:
        city = city.upper()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            if cacheSize > 0:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
            time += 5
    return time
