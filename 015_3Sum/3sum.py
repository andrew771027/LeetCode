class ThreeSum():

    def __init__(self):
        pass
    
    def method_1(self, nums, target):

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


if "__main__" == __name__:

    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    target = 0

    test = ThreeSum()
    result = test.method_1(nums=nums, target=target)
    print(result)