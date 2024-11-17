'''
1385. 两个数组间的距离值
https://leetcode.cn/problems/find-the-distance-value-between-two-arrays/description/
'''
# 解法1 暴力
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans= 0
        for i in arr1:
            flag= 0
            for j in arr2:
                if abs(i-j) <= d:
                    flag = -1
                    break
            if flag ==0:
                ans+=1
        return ans

# 解法2 二分查找
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


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        for x in arr1:
            p1 = right_bound(arr2, x + d) + 1  # 返回大于x+d的最小下标
            p2 = left_bound(arr2, x - d) - 1  # 返回小于x-d的最大下标
            if p1 - p2 <= 1:  # 如果下标开区间a和b之间有1个数，
                ans += 1
        return ans

