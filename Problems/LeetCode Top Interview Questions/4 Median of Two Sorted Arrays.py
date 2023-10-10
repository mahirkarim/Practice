class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # likely binary search, needs to be O(log(m+n))

        # could probably merge and sort
        # it's slow but python sort is O(nlogn)

        # this solution beats 14% speed, 79% memory
        # appears to be O((n+m)log(m+n))
        nums3 = nums1 + nums2
        nums3.sort()

        l_nums3 = len(nums3)
        print(nums3)
        if l_nums3 % 2 == 0:
            return (nums3[l_nums3 / 2 - 1] + nums3[l_nums3 / 2]) / 2.0

        return nums3[l_nums3 // 2]
    
        # maybe check both medians and then binary search lower

    # work in progress to make it O(log(n+m))
    # def findIndex(self, target, nums, above):
    #     len_nums = len(nums)

    #     if len_nums == 1:
    #         if nums[0] > target and not above:
    #             return 0
    #         elif nums[0] < target and not above:
    #             return 1
    #         elif nums[0] > target and above:
    #             return 1
    #         else:
    #             return 0

    #         return 1
    #     if len_nums % 2 == 0:
    #         idx = len_nums // 2 - 1
    #     else:
    #         idx = len_nums // 2
        
    #     if above:
    #         if nums[idx] > target:
    #             return findIndex(target, nums[0:idx],above)
    #         else:
    #             return idx + findIndex(target, nums[idx+1:], above)
    #     else:
    #         if nums[idx] > target:
    #             return findIndex(target, nums[0:idx],above)
    #         else:
    #             return -idx + findIndex(target, nums[idx+1:], above)

    # def findMedianSortedArrays(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: float
    #     """
    #     len1 = len(nums1)
    #     len2 = len(nums2)

    #     total = len1 + len2

    #     total_even = (total % 2 == 0)
    #     len1_even = (len1 % 2 == 0)

    #     if len1 % 2 == 0:
    #         idx1 = len1 // 2 - 1
    #     else:
    #         idx1 = len1 // 2

    #     if len2 % 2 == 0:
    #         idx2 = len2 // 2 - 1
    #     else:
    #         idx2 = len2 // 2

    #     target1 = nums1[idx1]
    #     target2 = nums2[idx2]

    #     if target1 == target2 and not total_even:
    #         return target1
    #     elif target1 == target2 and total_even and len1_even:
    #         if nums1[idx1 + 1] < nums2[idx2 + 1]:
    #             return (nums1[idx1 + 1] + target2) / 2.0
    #         else:
    #             return (target1 + nums2[idx2 + 1]) / 2.0

    #     if len1 >= len2:
    #         other_nums = nums1
    #         target = target1
    #         if target1 > target2:
    #             nums_check = nums2[idx2:]
    #         else:
    #             nums_check = nums2[0:idx2]
    #     else:
    #         other_nums = nums2
    #         target = target2
    #         if target1 < target2:
    #             nums_check = nums1[idx1:]
    #         else:
    #             nums_check = nums1[0:idx1]
        
    #     idx1, idx2 = findIndices(target, nums_check, other_nums))