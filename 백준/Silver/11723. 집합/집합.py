import sys

n = int(sys.stdin.readline())
s = set()

for _ in range(n):
    temp = sys.stdin.readline().strip().split(' ')
    
    if len(temp) == 1:
        cmd = temp[0]
        
        if cmd == 'all':
            s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
        else:  # cmd == 'empty'
            s.clear()  
  
    else:
        cmd = temp[0]
        num = int(temp[1])
        
        if cmd == 'add':
            s.add(num)
        elif cmd == 'remove':
            s.discard(num)
        elif cmd == 'check':
            print(1 if num in s else 0)
        else:  # cmd == 'toggle'
            if num in s:
                s.remove(num)
            else:
                s.add(num)