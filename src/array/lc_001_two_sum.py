from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        results: List = []

        for index, number in enumerate(nums):

            num_1: int = number
            num_2: int = target - num_1

            if num_2 in nums[index + 1 :]:
                results = [
                    nums.index(num_1),
                    nums[index + 1 :].index(num_2) + (index + 1),
                ]
                return results

        raise ValueError
