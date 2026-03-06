from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        start: int = 0
        end: int = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return start
