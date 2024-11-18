'''
209. 长度最小的子数组
https://leetcode.cn/problems/minimum-size-subarray-sum/description/
'''


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 不定长滑动窗口，每一个num都需判断，所以要用for
        ans = inf
        s=left=0
        for right,num in enumerate(nums):
            s += num
            while s-nums[left]>=target:
                s -= nums[left]
                left+=1
            if s>=target:
                ans = min(ans,right-left+1)
        return ans if ans <inf else 0

