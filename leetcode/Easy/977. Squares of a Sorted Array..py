"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.


Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?"""

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        size = len(nums)
        output = [None] * size
        left = 0
        right = size - 1
        for i in range(size-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                output[i] = nums[left] ** 2
                left += 1
            else:
                output[i] = nums[right] ** 2
                right -= 1
        return output


"""
Runtime: 391 ms, faster than 23.11% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.2 MB, less than 51.49% of Python3 online submissions for Squares of a Sorted Array.
"""

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([i**2 for i in nums])

"""
Runtime: 241 ms, faster than 78.63% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.3 MB, less than 18.75% of Python3 online submissions for Squares of a Sorted Array.
"""

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        size = len(nums)
        result = [0] * size
        index = size - 1
        l, r = 0, size - 1
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                result[index] = nums[r] * nums[r]
                r -= 1
            else:
                result[index] = nums[l] * nums[l]
                l += 1
            index -= 1
        return result

"""
Runtime: 222 ms, faster than 91.54% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.2 MB, less than 51.49% of Python3 online submissions for Squares of a Sorted Array.
"""