class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, maxP = 0, 0
        n = len(prices)
        l, r = 0, 1

        while r < n:
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max( maxP, profit)

            else:
                l = r
            r += 1
        return maxP