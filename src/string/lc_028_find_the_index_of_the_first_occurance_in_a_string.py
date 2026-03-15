class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        iterate from i to total length which is haystack.length() - needle.length() + 1
        validate the substring which length is needle.length()
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1
