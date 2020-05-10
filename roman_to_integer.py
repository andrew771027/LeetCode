class Solution:
    def romanToInt(self, s :str ) -> int:

        result = 0
        index = 0

        dictSpecialRoman = {}
        dictSpecialRoman["IV"] = 4
        dictSpecialRoman["IX"] = 9
        dictSpecialRoman["XL"] = 40
        dictSpecialRoman["XC"] = 90
        dictSpecialRoman["CD"] = 400
        dictSpecialRoman["CM"] = 900

        dictRoman = {}
        dictRoman["I"] = 1
        dictRoman["V"] = 5
        dictRoman["X"] = 10
        dictRoman["L"] = 50
        dictRoman["C"] = 100
        dictRoman["D"] = 500
        dictRoman["M"] = 1000

        try:

            while index < len(s)  :

                specialRoman = s[index] + s[index+1]
                
                if specialRoman in dictSpecialRoman:
                
                    result = result + dictSpecialRoman[specialRoman]
                    index = index + 2
                    
                else:
                    
                    result = result + dictRoman[s[index]]
                    index = index + 1

        except IndexError:
            result = result + dictRoman[s[index]]
        finally:
            return result


if __name__ == "__main__":

    o = Solution()
    strRoman = "MCMXCIV"
    value = o.romanToInt(strRoman)
    print(value)
