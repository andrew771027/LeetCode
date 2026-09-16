from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        result: List = []

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                result.append(s[i])
            else:
                if not result:
                    return False

                top = result.pop()

                if s[i] == ")" and top != "(":
                    return False
                if s[i] == "}" and top != "{":
                    return False
                if s[i] == "]" and top != "[":
                    return False

        return len(result) == 0
