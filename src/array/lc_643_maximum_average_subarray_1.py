class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        # Initialize currSum and maxSum to the sum of the initial k elements
        current_sum = sum(nums[:k])
        max_sum = current_sum

        # Start the loop from the kth element 
        # Iterate until you reach the end
        for i in range(k, len(nums)):

            # Subtract the left element of the window
            # Add the right element of the window
            current_sum += nums[i] - nums[i-k]

            # Update the max
            max_sum = max(max_sum, current_sum)

        # Since the problem requires average, we return the average
        return max_sum / k

