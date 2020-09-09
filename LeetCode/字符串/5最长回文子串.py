"""
暴力破解 超时
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        max_len = 1
        res = s[0]

        # 枚举所有长度大于等于 2 的子串
        for i in range(size - 1):
            for j in range(i + 1, size):
                if j - i + 1 > max_len and self.__valid(s, i, j):
                    max_len = j - i + 1
                    res = s[i:j + 1]
        return res

    def __valid(self, s, left, right):
        # 验证子串 s[left, right] 是否为回文串
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

def longestPalindrome(s: str) -> str:


if __name__ == '__main__':
	s = "babad"
	print(longestPalindrome(s))
	s = ""
	print(longestPalindrome(s))
	s = "cbbd"
	print(longestPalindrome(s))
	s = "b"
	print(longestPalindrome(s))
	s = "ccc"
	print(longestPalindrome(s))
	s = "abcba"
	print(longestPalindrome(s))