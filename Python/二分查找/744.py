'''
744. 寻找比目标字母大的最小字母
https://leetcode.cn/problems/find-smallest-letter-greater-than-target/description/
'''
# 时间复杂度：O(log n)，空间复杂度：O(1)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 大于target最小字符==target右边界+1
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return letters[right + 1] if right >= -1 and left < len(letters) else letters[0]
