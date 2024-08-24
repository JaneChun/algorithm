def solution(players, callings):
    positions = {name: i for i, name in enumerate(players)}
    # {'mumu': 0, 'soe': 1, 'poe': 2, 'kai': 3, 'mine': 4}
        
    for name in callings:
        idx = positions[name]
        prevName = players[idx - 1]
        
        # 딕셔너리 업데이트
        positions[name] = idx - 1
        positions[prevName] = idx
        
        # 배열 업데이트
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
        
    return players