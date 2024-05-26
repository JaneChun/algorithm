def solution(myString, pat):
    temp = myString.replace('A', '#').replace('B', 'A').replace('#','B')
    return int(pat in temp)