class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == "" and haystack == "":
            return 0
        
        if needle not in haystack:
            return -1
        
        for i in range(len(haystack)):

            length_neddle = len(needle)
            if haystack[i: i+length_neddle] == needle:
                return i

haystack = "hello"
needle = "ll"

haystack = "aaaaa"
needle = "bba"

haystack = ""
needle = ""

test = Solution()
result = test.strStr(haystack, needle)
print(result)