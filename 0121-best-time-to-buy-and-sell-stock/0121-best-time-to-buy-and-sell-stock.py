class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min = prices[0]
        # min_ind = 0
        # max_ind = len(prices)
        # max = 0

        profit = 0 
        buy = prices[0]

        for price in prices[1:]:
            if price > buy:
                profit = max(profit, price - buy)
            else:
                buy = price
        return profit

        # for index in range(1, len(prices)):
        #     # print(max)
        #     # print(min)
        #     if min > prices[index] and index < max_ind:
        #         min_ind = index
        #         min = prices[index]
        #     if max < prices[index] and index > min_ind:
        #         max = prices[index]
        #         max_ind = index
        # print("max " + str(max))
        # print("min " + str(min))
        # if max - min < 0: 
        #     return 0
        # else:
        #     return max - min