from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words: List = s.strip().split(" ")

        if len(words) == 0:
            return 0

        return len(words[-1])
