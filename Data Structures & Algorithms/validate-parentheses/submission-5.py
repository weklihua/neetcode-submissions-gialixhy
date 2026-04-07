class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        dict = {"}" : "{", "]":"[", ")" : "("}
        stack = deque()
        if s[0] in dict.keys() or s[-1] in dict.values():
            return False
        for char in s:
            stack.append(char)
            if char in dict.keys():
                a = stack.pop()
                b = stack.pop()
                if b != dict[a]:
                    return False
        if stack:
            return False
        return True