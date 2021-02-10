
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        从字符串的第一个元素开始，执行这个逻辑：
        a. 用一个变量保存当前已经发现的最大长度，假设名为maxLen；
        b. 如果当前检查的元素在窗口中没有，就加入窗口，例如窗口中已经有了"ab"，当前是"c"，那么窗口中最大长度加一；
        c. 如果当前检查的元素在窗口中存在，例如窗口中已经有了"abc"，当前检查的元素是"a"，这个"a"在窗口总已经存在了，窗口作调整，窗口中的"a"和它左侧的所有元素全部移除窗口，再把当前检查的"a"元素加入窗口；
        d. 拿当前窗口的长度和maxLen比较，大的值存入maxLen中；
        e. 继续检查字符串的下一个元素，逻辑是前面的步骤；
        '''

        s = list(s)
        tmpList = []
        maxList = []
        max = 0

        for i in range(len(s)):

            if s[i] not in tmpList:
                tmpList.append(s[i])
            else:
               n = tmpList.index(s[i])
               tmpList = tmpList[n+1:]
               tmpList.append(s[i])

            if len(tmpList) > max:
                max = len(tmpList)
                maxList = tmpList
        
        return len(maxList)

if __name__ == "__main__":

    # s = "abcabcbb"
    # s = "bbbbb"
    s = "pwwkew"

    test = Solution()
    length = test.lengthOfLongestSubstring(s)
    print(length)
