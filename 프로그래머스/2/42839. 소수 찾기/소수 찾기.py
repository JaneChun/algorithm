from itertools import permutations

def solution(numbers):
    numbers_set = set()
    
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        numbers_set.update([int(''.join(p)) for p in perms])
        
    return len(list(filter(lambda x: is_prime(x),numbers_set)))
        
        
        
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True