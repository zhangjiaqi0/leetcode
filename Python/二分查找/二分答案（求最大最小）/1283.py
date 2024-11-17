'''
1283. 使结果不超过阈值的最小除数
https://leetcode.cn/problems/find-the-smallest-divisor-given-a-threshold/description/
'''
# 时间复杂度：O(nlogU)，其中 n 是 nums 的长度，U=max(nums)。二分 O(logU) 次，每次 O(n) 遍历 nums。
# 空间复杂度：O(1)
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # 由于除数越大，元素和越大，有单调性，可以使用二分答案
        # 元素和<=threshold的m就是答案
        left, right = 0, max(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if sum((x - 1) // mid for x in nums) <= threshold - len(nums):
                right = mid
            else:
                left = mid
        return right


