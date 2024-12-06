class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Time: O(n)
        #Space: O(1)

        min_price = float(inf)
        max_profit = 0

        for i in prices:
            if i < min_price:
                min_price = i
            
            profit = i - min_price

            if profit > max_profit:
                max_profit = profit
        
        return max_profit

        
        ''' Brute Force from my brain which didnt pass testcase 154
        # buy when its the lowest and sell when its the highest
        buy = min(prices)
        sell = 0
        # if the last day has the minimum stock price(buy) then no profits
        if prices.index(buy) == len(prices)-1:  
            return 0
        # after finding the minmum we have to pick the maximum stock price(sell) form the remaining days
        else:
            for i in range(prices.index(buy),len(prices)): # the range is the days after buying the stock
                #find max or sell just comapring and updating
                if prices[i]>sell:
                    sell = prices[i]

            # calculate the profit           
            profit = sell-buy
            return profit'''