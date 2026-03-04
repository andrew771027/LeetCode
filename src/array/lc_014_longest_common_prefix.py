from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs: List = sorted(strs)
        first_str: str = sorted_strs[0]
        last_str: str = sorted_strs[-1]
        common_prefix: str = ""

        for i in range(min(len(first_str), len(last_str))):
            if first_str[i] == last_str[i]:
                common_prefix += first_str[i]
            else:
                break

        return common_prefix
