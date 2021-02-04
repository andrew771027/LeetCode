def Three_Sum_Closet_Basic(nums, target):

    result = float("inf")
    nums.sort()
    
    for first in range(len(nums)-2):

        second = first + 1
        third = len(nums) - 1

        while second < third:

            _sum = nums[first] + nums[second] + nums[third]
            
            if abs (result - target) > abs(_sum - target): 
                result = _sum

            if _sum > target:
                third -= 1
            else:
                second +=1


    return result

if "__main__" == __name__:

    nums = [-1,2,1,-4]
    target = 1

    min_sum = Three_Sum_Closet_Basic(nums=nums, target=target)
    print(min_sum)