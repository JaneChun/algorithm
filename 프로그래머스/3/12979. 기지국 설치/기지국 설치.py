import math

def solution(n, stations, w):
    answer = 0

    network_apts = [[max(1, i - w), min(n, i + w)] for i in stations]
    # print('network_apts', network_apts)
    
    no_network_apts = []
    i = 1
    for s, e in network_apts:
        no_network_apts.append([i, min(n, s - 1)])
        i = e + 1
        
    if i <= n:
        no_network_apts.append([i, n])
    # print('no_network_apts', no_network_apts)
    
    for s, e in no_network_apts:
        length =  e - s + 1
        coverage =  w * 2 + 1
        answer += math.ceil(length / coverage)

    return answer