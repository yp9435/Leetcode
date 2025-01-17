class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Base Case
        if len(s) != len(t):
            return False
        
        count = [0]*26
        
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        return set(count) == {0}