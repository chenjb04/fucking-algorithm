
from typing import List

"""
最大利润=max{前一天最大利润, 今天的价格 - 之前最低价格}
"""
def maxProfit(prices: List[int]) -> int:
	if not prices:
		return 0
	dp = [0] * (len(prices))
	min_price = prices[0]
	for i in range(1, len(prices)):
		min_price = min(min_price, prices[i])
		dp[i] = max(dp[i-1], prices[i] - min_price)
	return dp[-1]


if __name__ == '__main__':
	prices = [7,1,5,3,6,4]
	print(maxProfit(prices))