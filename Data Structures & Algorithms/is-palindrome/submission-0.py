class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join(c for c in s if c.isalnum()).lower()
        for i in range(len(filtered)):
            if filtered[i] != filtered[len(filtered) - i - 1]:
                return False
        return True

        