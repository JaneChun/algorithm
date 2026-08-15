import re

class Solution:
    def romanToInt(self, s: str) -> int:
        normal = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        special = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }

        keys = [*special.keys(), *normal.keys()]
        # ['IV', 'IX', 'XL', 'XC', 'CD', 'CM', 'I', 'V', 'X', 'L', 'C', 'D', 'M']

        pattern = f"{'|'.join(keys)}"
        # IV|IX|XL|XC|CD|CM|I|V|X|L|C|D|M

        splitted = re.findall(pattern, s)
        # ['M', 'CM', 'XC', 'IV']

        result = 0
        for roman in splitted:
            if roman in special:
                result += special[roman]
            else:
                result += normal[roman]
        
        return result