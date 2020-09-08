"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 

示例 1: 

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。


示例 2: 

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。


示例 3: 

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

Related Topics 哈希表 双指针 字符串 Sliding Window
"""

from typing import List


def lengthOfLongestSubstring(s: str) -> int:
    if not s:
    	return 0
        # 保存滑动窗口字符串
    window = []
    # 滑动窗口长度
    window_len = 0
    # 最大字串长度
    max_len = 0
    for i in range(len(s)):
        # 如果当前值不在窗口中，添加
        if s[i] not in window:
            window.append(s[i])
            # 窗口长度+1
            window_len += 1
        else:
            # 获取在窗口中的位置
            index = window.index(s[i])
            # 移除窗口中当前位置之前的元素
            window = window[index + 1:]
            # 加入当前值
            window.append(s[i])
            # 更新当前窗口长度
            window_len = len(window)
    # 如果当前长度 大于最大字串长度，更新最大字串长度
        if window_len > max_len:
            max_len = window_len
    return max_len



if __name__ == '__main__':
	s = "abcabcbb"
	print(lengthOfLongestSubstring(s))
	s = "pwwkew"
	print(lengthOfLongestSubstring(s))