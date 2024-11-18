'''
1011. 在 D 天内送达包裹的能力
https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/description/
'''
# 时间复杂度：O(nlogU)，其中 n 是 nums 的长度，U=max(nums)。二分 O(logU) 次，每次 O(n) 遍历 nums。
# 空间复杂度：O(1)
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 载重越大，所需要的天数越少，具有单调性，二分载重
        l = max(weights)
        r = sum(weights)

        def check(mid):
            cnt = 0
            s = 0
            for x in weights:
                if s + x > mid:
                    cnt += 1
                    s = x
                else:
                    s += x
            cnt += 1
            return cnt <= days

        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l


