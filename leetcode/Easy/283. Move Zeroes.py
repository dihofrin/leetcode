"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?"""

# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        nonzero = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[nonzero] == 0:
                nums[i], nums[nonzero] = nums[nonzero], nums[i]
            if nums[nonzero] != 0:
                nonzero += 1

"""Runtime: 177 ms, faster than 81.71% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.5 MB, less than 97.27% of Python3 online submissions for Move Zeroes."""""

def move_zeroes(nums):
    result = []
    for i in nums:
        if i != 0:
            result.append(i)
    result.extend((len(nums) - len(result)) * [0])
    return result

"""Runtime: 264 ms, faster than 39.25% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.6 MB, less than 17.33% of Python3 online submissions for Move Zeroes."""