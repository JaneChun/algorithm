def solution(wallpaper):
    answer = []
    
    top = len(wallpaper) - 1
    bottom = 0
    left = len(wallpaper[0]) - 1
    right = 0
    
    for rowIdx in range(len(wallpaper)):
        for colIdx in range(len(wallpaper[0])):
            if wallpaper[rowIdx][colIdx] == '#':
                if rowIdx < top:
                    top = rowIdx
                if rowIdx > bottom:
                    bottom = rowIdx
                if colIdx < left:
                    left = colIdx
                if colIdx > right:
                    right = colIdx
                
    return [top, left, bottom + 1, right + 1]