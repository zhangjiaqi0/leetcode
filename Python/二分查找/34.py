'''
34. 在排序数组中查找元素的第一个和最后一个位置
https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/
'''
# 时间复杂度：O(log n)，空间复杂度：O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_bound(nums, target):  # 找到小于target的最后一个数，== >=target-1
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left+(right-left) // 2
                if nums[mid] < target:
                    left = mid+1# 确保left返回的是==target的第一个数的索引
                else:
                    right = mid-1# 当left==right时，退出循环，说明找第一个数的索引
            return left if left<len(nums) and nums[left]==target else -1

        def right_bound(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left+(right-left) // 2
                if nums[mid] >target: right = mid-1
                else: left = mid+1
            return right if right >=0  and nums[right]==target else -1

        start = left_bound(nums, target)
        right = right_bound(nums, target)
        return [start, right]
