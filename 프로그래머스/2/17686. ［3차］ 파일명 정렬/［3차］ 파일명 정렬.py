def solution(files):
    splitted = []
    
    for file in files:
        head = ''
        number = ''
        tail = ''
        for char in file:
            if not char.isdigit() and number == '':
                head += char
            elif char.isdigit() and tail == '':
                number += char
            else:
                tail += char
        splitted.append([head, number, tail])
          
    sorted_splitted = sorted(splitted, key=lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(arr) for arr in sorted_splitted]
