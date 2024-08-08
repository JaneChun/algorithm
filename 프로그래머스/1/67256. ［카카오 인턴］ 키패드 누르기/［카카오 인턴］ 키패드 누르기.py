keypad = {
    '1': (0, 0), '2': (0, 1), '3': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '7': (2, 0), '8': (2, 1), '9': (2, 2),
    '*': (3, 0), '0': (3, 1), '#': (3, 2)
    }

def solution(numbers, hand):
    leftHand = '*'
    rightHand = '#'
    answer = ''
    
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            leftHand = str(number)
        elif number in [3, 6, 9]:
            answer += 'R'
            rightHand = str(number)
        else:
            closerHand = findCloserHand(str(number), leftHand, rightHand)
            if closerHand == 'S':
                if hand == 'left':
                    answer += 'L'
                    leftHand = str(number)
                else:
                    answer += 'R'
                    rightHand = str(number)
            elif closerHand == 'L':
                answer += 'L'
                leftHand = str(number)
            else:
                answer += 'R'
                rightHand = str(number)
        
    return answer

def manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])
    
def findCloserHand(target, left, right):
    leftDistance = manhattan_distance(keypad[target], keypad[left])
    rightDistance = manhattan_distance(keypad[target], keypad[right])

    if leftDistance < rightDistance: 
        return 'L'
    elif leftDistance > rightDistance: 
        return 'R'
    else:
        return 'S'