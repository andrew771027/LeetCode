import pytest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        
        if len(b) > len(a):
            a = "0" * (len(b) - len(a)) + a

        carry = 0
        result = ""

        for index in range(len(a) -1, -1 ,-1):

            added = int(a[index]) + int(b[index]) + int(carry)

            result = str(added % 2) + result
            carry = added // 2

            # if added == 0:
            #     result = "0" + result 
            #     carry = 0
            
            # if added == 1:
            #     result = "1" + result
            #     carry = 0
            
            # if added == 2:
            #     result = "0" + result
            #     carry = 1
            
            # if added == 3:
            #     result = "1" + result
            #     carry = 1
        
        if carry == 1:
            result = "1" + result

        return result

@pytest.mark.parametrize(("parma_a" ,"parma_b", "expected_result"), [
    ("0", "0", "0"),
    ("1", "1", "10"),
    ("11", "1", "100"),
    ("1010", "1011", "10101")
])
def test_add_binary(parma_a, parma_b, expected_result):

    test = Solution()
    assert expected_result == test.addBinary(a=parma_a, b=parma_b)