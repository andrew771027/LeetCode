class ThreeSum():

    def __init__(self):
        pass
    
    def method_basic(self, nums, target):

        result = []
        i = 0

        while (i < len(nums)):
            j = i + 1
            while (j < len(nums)):
                k = j + 1
                while (k < len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:                      
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()

                        if temp not in result:
                            result.append(temp)
                    k+=1
                j+=1
            i+=1
        
        return result

    def method_advance(self, nums, target):

        result = []
        nums.sort()

        for first in range(len(nums)-2):

            second = first + 1
            third = len(nums) - 1

            while second < third:

                if nums[first] + nums[second] + nums[third] == 0:
                    temp = [nums[first], nums[second], nums[third]]
                    temp.sort()
                    if temp not in result:
                        result.append(temp)

                    second += 1
                    third -= 1

                elif nums[second] + nums[third] < nums[first] * -1:
                    second += 1
                elif nums[second] + nums[third] > nums[first] * -1:
                    third -= 1 
                else:
                    pass

        return result


if "__main__" == __name__:

    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    target = 0

    test = ThreeSum()
    # result = test.method_basic(nums=nums, target=target)
    result = test.method_advance(nums=nums, target=target)
    print(result)