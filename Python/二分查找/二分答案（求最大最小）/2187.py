'''
2187. 完成旅途的最少时间
https://leetcode.cn/problems/minimum-time-to-complete-trips/description/
'''

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # 时间越多，完成的旅途越多，有单调性，可以二分答案
        min_t = min(time)
        avg = (totalTrips - 1) // len(time) + 1
        left = min_t * avg - 1
        right = min(max(time) * avg, min_t * totalTrips)
        while left + 1 < right:
            mid = (left + right) // 2
            if sum(mid // t for t in time) >= totalTrips:
                right = mid
            else:
                left = mid
        return right
