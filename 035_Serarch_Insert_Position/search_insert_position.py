import pytest



# class TestSolution:


#     @pytest.mark.parameterize("nums", "target", "expected_result", [
#         ([1, 3, 5, 6], 5, 2),
#         ([1, 3, 5, 6], 2, 1),
#         ([1, 3, 5, 6], 7, 4),
#         ([1, 3, 5, 6], 0, 0),
#         ([], 0, 0)
#     ])
#     def test_method_basis(self, nums, target: int) -> int:
#         '''
#         Using for loop to traversal all nums
#         '''
#         result = 0

#         for index in range(len(nums)):
            
#             try:
            
#                 if nums[index] < target and nums[index+1] > target:
#                     result = index
#                     break
                
#                 elif nums[index] == target:
#                     result = index
#                     break 
            
#             except:
#                 result = len(nums)
        
#         assert result == expected_result

class Solution:

    def method_basic(self, nums, target: int) -> int:
        '''
        Use for loop to traversal all nums
        '''
        result = 0

        if nums[-1] < target:
            return len(nums)

        for index in range(len(nums)):
            
            if nums[index] < target and nums[index+1] > target:
                return index + 1
            
            elif nums[index] == target:
                return index
        
        return 0

    def method_advance(self, nums, target: int) -> int:
        '''
        Use binary search 
        '''

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
            
            
        return left


test = Solution()

# nums = [1, 3, 5, 6]
# target = 5
# expected =  2

# nums = [1, 3, 5, 6]
# target = 2
# expected =  1

nums = [1, 3, 5, 6]
target = 7
expected =  4

result = test.method_basic(nums, target)
assert result == expected