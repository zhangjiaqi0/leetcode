'''
1870. 准时到达的列车最小时速
https://leetcode.cn/problems/minimum-speed-to-arrive-on-time/description/
'''
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # sum(dist-1//t +1)>=hour
        # 时速越大，花费时间越小，单调性，二分时速
        n = len(dist)
        h100 = round(hour * 100)  # 下面不会用到任何浮点数
        delta = h100 - (n - 1) * 100
        if delta <= 0:  # 无法到达终点
            return -1 # 每趟列车至少花费1小时，最后一趟严格大于0

        max_dist = max(dist)
        if h100 <= n * 100:  # 特判
            # 见题解中的公式
            return max(max_dist, (dist[-1] * 100 - 1) // delta + 1)

        def check(v: int) -> bool:
            t = n - 1  # n-1 个上取整中的 +1 先提出来
            for d in dist[:-1]:
                t += (d - 1) // v
            return (t * v + dist[-1]) * 100 <= h100 * v

        left = (sum(dist) * 100 - 1) // h100  # 也可以初始化成 0（简单写法）
        h = h100 // (n * 100)
        right = (max_dist - 1) // h + 1  # 也可以初始化成 max_dist（简单写法）
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right

