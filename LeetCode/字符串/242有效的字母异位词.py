"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。
"""

"""
解题思路：
	1、先把字符串s依次遍历存入一个dict中，key为字符，value为每个字符出现的次数
	2、再把字符串t依次遍历存入一个dict中，key为字符，value为每个字符出现的次数
	3、比较两个dict，相同为True,不同为False
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        dic1 = {}
        for i in s:
            if dic.get(i) is None:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in t:
            if dic1.get(i) is None:
                dic1[i] = 1
            else:
                dic1[i] += 1
        if dic == dic1:
            return True
        return False