'''
28. 找出字符串中第一个匹配项的下标
https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
'''
# 解法1 find函数，时间复杂度：O(n*m)，空间复杂度：O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# 解法2 切片
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
