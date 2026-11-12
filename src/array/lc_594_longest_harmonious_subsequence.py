class Solution:
    def findLHS(self, nums: list[int]) -> int:
        frequencies: dict[int, int] = {}

        # Step 1: Count frequency
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        # Step 2: Find longest harmonious subsequence
        max_length = 0

        for num, frequency in frequencies.items():
            if num + 1 in frequencies:
                length = frequency + frequencies[num + 1]
                max_length = max(max_length, length)

        return max_length
    