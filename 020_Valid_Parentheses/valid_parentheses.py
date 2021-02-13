class Solution:

    def isValid(self, s: str) -> bool:

        stack = []
        left = ["(", "[", "{"]
        right = [")", "]", "}"]
        result = False

        if len(s) % 2 != 0:
            result = False
            return result

        for i in range(len(s)):

            if s[i] in left:
                stack.append(s[i])
    
            elif s[i] in right:
                
                if len(stack) == 0:
                    result = False
                    break

                left_bracket = stack.pop()

                if left_bracket == "(" and s[i] == ")":
                    result = True
                elif left_bracket == "[" and s[i] == "]":
                    result = True
                elif left_bracket == "{" and s[i] == "}":
                    result = True
                else:
                    result = False
                    break

        if len(stack) != 0:
            result = False
            return result

        return result
    
# s = r"()"
# s = r"()[]{}"
# s = r"(]"
# s = r"([)]"
# s = r"{[]}"
s = r"(){}}{"
# s = r"([]){"
# s = r"[[[]"

test = Solution()
result = test.isValid(s)
print(result)