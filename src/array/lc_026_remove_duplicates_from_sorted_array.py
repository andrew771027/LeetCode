from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:  # Handle empty list case
            return 0

        j: int = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1  # Move to the next position for unique element
                nums[j] = nums[i]  # Assign the unique element

        return j + 1
