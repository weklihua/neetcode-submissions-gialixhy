class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        for c in s:
            s_map[c] = s_map.get(c, 0) + 1
        
        for char in t:
            
            s_map[char] = s_map.get(char, 0) - 1
            if s_map[char] < 0:
                return False
        for val in s_map.values():
            if val != 0:
                return False
        return True

        