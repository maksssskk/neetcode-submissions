class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_price = 0

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                curr_price = prices[r] - prices[l]
                max_price = max(curr_price, max_price)
            else:
                l = r
        return max_price