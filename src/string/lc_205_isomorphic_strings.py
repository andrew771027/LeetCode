from typing import List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        建立s & t個別的index: List
        如果s & t 每一個char要出現過
        則在index: List 該對應的位置做標記 (+1 aka 次數)
        位置則由char的ascii決定
        """

        index_s: List = [0] * 200
        index_t: List = [0] * 200

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if index_s[ord(s[i])] != index_t[ord(t[i])]:
                return False

            index_s[ord(s[i])] = i + 1
            index_t[ord(t[i])] = i + 1

        return True
