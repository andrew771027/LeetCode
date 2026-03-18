from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        建立1個index: List
        在index: List 該對應的位置做標記 (+1 aka 次數)
        在index: List 該對應的位置做標記 (-1 aka 次數) (如果有重複出現)
        位置則由char的ascii決定
        如果在index裡有不為0的值，則不是Anagram
        """
        if len(s) != len(t):
            return False

        array: List = [0] * 26

        for i in range(len(s)):
            array[ord(s[i]) - ord("a")] += 1
            array[ord(t[i]) - ord("a")] -= 1

        for check in array:
            if check != 0:
                return False
        return True
