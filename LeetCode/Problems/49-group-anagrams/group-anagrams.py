from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        tuple_dict = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            tuple_dict[key].append(word)
        
        return [list(x) for x in tuple_dict.values()]