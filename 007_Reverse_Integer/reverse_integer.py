class Solution:
    def reverse(self, x: int) -> int:

        result = 0
        x = str(x)
        sign = "+"

        if x.startswith("-"):
            sign = "-"
            x = x.replace("-", "")

        for index in range (0, len(str(x)) ):
            
            ch = int(x[index]) 
            result = result + ( ch * (10**index))

        if sign == "-":
            result = -1 * result

        if result > (2 ** 31) -1 or result <  (-2**31):
            result = 0
            
        return result



o = Solution()
input = 1534236469
result = o.reverse(input)
print(result)