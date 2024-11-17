'''
2529. 正整数和负整数的最大计数
https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/description/
'''
# 解法1 遍历，时间复杂度：O(n)，空间复杂度：O(1)
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos, neg = 0, 0
        for n in nums:
            if n > 0:
                pos += 1
            elif n < 0:
                neg += 1
        return pos if pos >= neg else neg


# 解法2 二分查找，时间O(log n)，空间0(1)
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def left_bound(nums, target):  # 找到小于target的最后一个数，== >=target-1
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1  # 确保left返回的是==target的第一个数的索引
                else:
                    right = mid - 1  # 当left==right时，退出循环，说明找第一个数的索引
            return left

        def right_bound(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right

        neg = left_bound(nums, 0)
        pos = len(nums) - right_bound(nums, 0) - 1
        return max(neg, pos)
