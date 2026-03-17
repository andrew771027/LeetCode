from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s: List = []
        carry: int = 0
        i: int = len(a) - 1
        j: int = len(b) - 1

        while i >= 0 or j >= 0 or carry == 1:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1

            s.append(str(carry % 2))
            carry //= 2

        return "".join(reversed(s))
