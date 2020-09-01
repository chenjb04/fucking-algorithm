"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。 



示例： 

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2




提示：你可以假定该字符串只包含小写字母。 
Related Topics 哈希表 字符串

"""

"""
hash: 遍历字符串，如果字符不在hash中，加入hash，key为字符：value为索引
如果字符存在hash中，那么value可以设为长度,最后返回最小索引
"""
def firstUniqChar(s: str) -> int:
	if not s:
		return -1
	hash_map = {}
	n = len(s)
	for i in range(n):
		if s[i] not in hash_map:
			hash_map[s[i]] = i
		else:
			hash_map[s[i]] = n
	if min(hash_map.values()) == n:
		return -1
	return min(hash_map.values())


if __name__ == '__main__':
	s = "leetcode"
	print(firstUniqChar(s))
	s = "loveleetcode"
	print(firstUniqChar(s))
	s = "aadadaad"
	print(firstUniqChar(s))