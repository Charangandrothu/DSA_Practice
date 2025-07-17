class Solution(object):
    def maxProfit(self,prices):
        min_price=float('inf')
        maxProfit=0
        for price in prices:
            if price<min_price:
                min_price=price
            elif price-min_price>maxProfit:
                maxProfit=price-min_price
        return maxProfit
        