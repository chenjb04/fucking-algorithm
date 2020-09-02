"""
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5
 

提示：

0 <= n <= 100
"""


"""
递归 会超时
"""
def fib(n: int) -> int:
	if n < 2:
		return n
	return (fib(n-1) + fib(n-2)) % 1000000007


"""
动态规划
"""
def fib1(n: int) -> int:
	dp = {}
	dp[0] = 0
	dp[1] = 1
	if n >=2 :
		for i in range(2, n+1):
			dp[i] = dp[i-1] + dp[i-2]
	return dp[n] % 1000000007


if __name__ == '__main__':
	n = 5
	print(fib(n))
	print(fib1(n))