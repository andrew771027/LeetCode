class FourSum():

    def __init__(self):
        pass

    def get_three_sum(self, nums, target):

        result = []
        nums.sort()

        for first in range(len(nums)-2):

            second = first + 1
            third = len(nums) - 1

            while second < third:

                if nums[first] + nums[second] + nums[third] == target:
                    temp = [nums[first], nums[second], nums[third]]
                    temp.sort()
                    if temp not in result:
                        result.append(temp)

                    second += 1
                    third -= 1

                elif nums[second] + nums[third] < target - nums[first]:
                    second += 1
                elif nums[second] + nums[third] > target - nums[first]:
                    third -= 1 
                else:
                    pass

        return result
    
    def method_basic(self, nums, target):

        result = []
        nums.sort()

        for i in range(len(nums)):
            
            flag = nums[i]
            rest_nums = nums[i+1:]

            three_sum = self.get_three_sum(nums=rest_nums, 
                                           target=target-flag)

            for j in range(len(three_sum)):

                temp = [nums[i]] + three_sum[j]

                if temp not in result:
                    result.append(temp)
                    # print(result)

        return result

if "__main__" == __name__:

    nums = [1, 0, -1, 0, -2, 2]
    # nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    target = 0

    test = FourSum()
    result = test.method_basic(nums=nums, target=target)
    # result = test.method_advance(nums=nums, target=target)
    print(result)
    
