import pytest

class Solution:

    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"
        else:
            last_string = self.countAndSay(n-1)

            result = ""
            count = 1
            for index in range(len(last_string)):

                if index != len(last_string) -1 and last_string[index] == last_string[index+1]:
                    count +=1
                else:
                    result = result + str(count) + last_string[index]
                    count = 1

            return result

@pytest.mark.parametrize(("param", "expected_result"), [
    (1, "1"),
    (2, "11"),
    (3, "21"),
    (4, "1211"),
    (5, "111221"),
    (6, "312211")
])
def test_count_and_say(param, expected_result):

    test = Solution()
    assert test.countAndSay(param) == expected_result


