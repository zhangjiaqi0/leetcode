'''
2300. 咒语和药水的成功对数
https://leetcode.cn/problems/successful-pairs-of-spells-and-potions/description/
'''
# 时间复杂度：O((n+m)logm)，其中 n 为 spells 的长度，m 为 potions 的长度。排序 O(mlogm)。二分 n 次，每次 O(logm)
# 空间复杂度：O(1)
def right_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return right


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        ans = []
        potions.sort()
        for i in spells:

            if i * potions[-1] < success:
                ans.append(0)
                continue
            # arr = [i*j for j in potions] # 超时
            success -= (
                1  # 为了避免讨论a能否被b整除问题，将>=success/i转化为>(success-1)/i
            )
            left = right_bound(potions, success // i) + 1
            ans.append(len(potions) - left)
        return ans
