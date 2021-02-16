import pytest

'''
首先我們只要先比對第一個跟第二個就可以知道，是否符合條件繼續比對下去，因為如果第一個跟第二個完全沒有相同的prefix的話，後面也不用比了，直接回傳空字串。
那如果第一個跟第二個比對完以後出現了我們要的prefix，那後面就用這組prefix去做篩選

Ref:https://medium.com/leetcode-%E6%BC%94%E7%AE%97%E6%B3%95%E6%95%99%E5%AD%B8/005-longest-common-prefix-%E6%89%BE%E5%B0%8B%E6%9C%80%E9%95%B7%E5%85%B1%E5%90%8C%E5%89%8D%E5%A2%9C-c7c1d1a2617a
'''
class Solution:
    def longestCommonPrefix(self, strs : list) -> str:
        
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        strs.sort(key=len)
        common_str = strs[0]
        
        for index in range(1, len(strs)):

            while strs[index].startswith(common_str) == False:

                common_str = common_str[:-1]
        
        return common_str

@pytest.mark.parametrize(("param","expected_result"),[
                                                        ([""], ""),
                                                        (["flower", "flow", "flight"], "fl"),
                                                        (["dog", "racecar", "car"], "")
                                                    ])              
def test_longest_common_prefix(param, expected_result):

    test = Solution()
    assert test.longestCommonPrefix(param) == expected_result