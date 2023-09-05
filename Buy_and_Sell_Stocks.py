'''
Buy and Sell Stock:

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

'''
class Solution:
    def maxProfit(self, prices):
        min_price = float('inf') # initialize minimum price to positive infinity
        max_profit = 0 # initialize maximum profit to zero
        
        for price in prices: # loop through each price in the list
            if price < min_price: # if price is less than minimum price so far
                min_price = price # update minimum price
            elif price - min_price > max_profit: # if selling price - buying price is greater than max profit so far
                max_profit = price - min_price # update max profit
        
        return max_profit # return the maximum profit
s=Solution()
print(s.maxProfit([5,7,2,9,3,11]))