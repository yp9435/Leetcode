from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        results = []

        for i in strs:
            sorted_s = tuple(sorted(i))
            hashmap[sorted_s].append(i)
        
        for i in hashmap.values():
            results.append(i)
        
        return results