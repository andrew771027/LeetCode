from typing import List


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        result: List = []

        while columnNumber > 0:
            columnNumber -= 1
            remainder: int = columnNumber % 26
            columnNumber //= 26
            result.append(chr(ord("A") + remainder))

        return "".join(reversed(result))
