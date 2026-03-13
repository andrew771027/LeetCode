from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        性質 1：自己 XOR 自己會變 0 -> a ^ a = 0
        性質 2：任何數 XOR 0 會是自己 -> a ^ 0 = a
        性質 3：交換律與結合律 -> a ^ b ^ a = (a ^ a) ^ b
        """

        result = 0

        for num in nums:
            result = result ^ num

        return result
