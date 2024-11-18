'''
30. 串联所有单词的子串
https://leetcode.cn/problems/substring-with-concatenation-of-all-words/description/
'''


from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 定长滑动窗口+判断word出现的次数
        window = len(words)*len(words[0])
        ans =[]
        start=0
        cnt_words = Counter(words)
        # print(cnt_words)
        # tmp_words = {word:0 for word in words}
        # print(tmp_words)
        while start< len(s)-window+1:
            tmp_words = {word:0 for word in words}
            for i in range(start,start+window, len(words[0])):
                tmp = s[i:i+len(words[0])]
                if tmp in cnt_words:
                    tmp_words[tmp]+=1
                else:
                    break
            if tmp_words == cnt_words:
                ans.append(start)
            start+=1
        return ans