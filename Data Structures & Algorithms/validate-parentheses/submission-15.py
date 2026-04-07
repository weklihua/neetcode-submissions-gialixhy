class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', '}': '{', ']':'['}
        charStack = deque()
        if len(s) < 2 or s[0] not in brackets.values():
            return False

        for char in s:
            if char in brackets.values():
                charStack.append(char)
            if char in brackets.keys():
                if not charStack:
                    return False
                curr = charStack.pop()
                if curr != brackets[char]:
                    return False
                
        if len(charStack) != 0:
            return False
        return True

