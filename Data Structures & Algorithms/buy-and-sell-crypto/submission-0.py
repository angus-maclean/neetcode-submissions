class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # two pointers
        # sliding window

        # initialise two pointers
        l, r = 0, 1
        # keep track of max profit 
        max_profit = 0

        # loop until the right pointer gets to the end
        while r < len(prices):
            # if the buy price is less than the sell price ie made a profit
            if prices[l] < prices[r]:
                # then the profit is difference
                profit = prices[r] - prices[l]
                # and we update max profit to be the new profit if it is higher than the current max profit
                max_profit = max(max_profit, profit)
            else:
                # else if the sell price is higher than buy price, move the left pointer over to where the right one is
                l = r
            # and increment the right pointer over
            r += 1
        # at the end of the loop return what the max profit was
        return max_profit
