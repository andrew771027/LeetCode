class Solution:
    def isPalindrome(self, s: str) -> bool:

        import re

        s = re.sub("[^A-Za-z0-9]", "", s).lower()

        start: int = 0
        end: int = len(s) - 1

        while start <= end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True
