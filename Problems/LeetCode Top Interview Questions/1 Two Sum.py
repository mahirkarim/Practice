# https://leetcode.com/problems/two-sum/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions


# below solution works faster than 47%, less memory than 79%
# def twoSum(nums, target):
#     """
#     nums: List[int]
#     target: int

#     return List[int]
#     """

#     x = len(nums)
#     for i in range(x):
#         num1 = nums[i]
#         for j in range(i+1, x):
#             if num1 + nums[j] == target:
#                 return [i, j] 
    
# below solution does not work because of negative numbers. 
# def twoSum(nums, target):
    # nums2 = filter(lambda x : x <= target, nums)

    # x = len(nums2)
    # for i in range(x):
    #     num1 = nums2[i]
    #     for j in range(i+1, x):
    #         num2 = nums2[j]
    #         if num1 + num2 == target:
    #             idx1 = nums.index(num1)
    #             idx2 = nums.index(num2)
                
    #             if idx1 != idx2:
    #                 return [idx1,idx2]
    #             else:
    #                 nums.pop(idx1)
    #                 return [idx1, nums.index(num2) + 1]

# this solution faster than 57%, less memory than 79%
# probably some sort of way to use the original nums list against 
# sorted list to make it faster (but more memory)
class Solution(object):
    def return_vals(self, num1, num2, nums):
            if num1 != num2:
                return [nums.index(num1), nums.index(num2)]
            else:
                idx1 = nums.index(num1)
                nums.pop(idx1)
                idx2 = nums.index(num2)
                return [idx1, idx2 + 1]

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = len(nums)
        nums2 = list(nums)
        nums2.sort()

        max = nums2[-1]
        
        for i in range(x): 
            num1 = nums2[i]
            if num1 + max < target:
                continue
            
            mid = x - ((x - i) / 2)
            if mid == x:
                mid -= 1
            if num1 + nums2[mid] > target:
                for j in range(i+1, mid):
                    if num1 + nums2[j] == target:
                        return(self.return_vals(num1, nums2[j],nums))
            else:
                for j in range(mid, x):
                    if num1 + nums2[j] == target:
                        return(self.return_vals(num1, nums2[j],nums))

