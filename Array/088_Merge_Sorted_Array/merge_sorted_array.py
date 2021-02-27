class Solution:

    def merge(self, nums1 , m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        index = 0
        for m in range(m, len(nums1)) :

            nums1[m] = nums2[index]
            index += 1
        
        for i in range (len(nums1)):
            for j in range(i+1, len(nums1)):

                if nums1[j] < nums1[i]:

                    temp = nums1[i] 
                    nums1[i] = nums1[j]
                    nums1[j] = temp

        return nums1


# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0


nums1 = [2,0]
m = 1
nums2 = [1]
n = 1

test = Solution()
result = test.merge(nums1, m, nums2, n)
print(result)