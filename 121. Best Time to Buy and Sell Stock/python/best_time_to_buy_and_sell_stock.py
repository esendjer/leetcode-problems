from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = 0
        max_prof = 0
        for i in range(1,len(prices)):
            if max_prof < prices[i] - prices[min_p]:
                max_prof = prices[i] - prices[min_p]
            if prices[i] < prices[min_p]:
                min_p = i
        return max_prof

    def maxProfitBL(self, prices: List[int]) -> int:
        min_p = 0
        max_prof = 0
        for i in range(1,len(prices)):
            pmi = prices[i] - prices[min_p]
            max_prof = pmi * (max_prof < pmi) + max_prof * (max_prof >= pmi)
            min_p = i * (prices[i] < prices[min_p]) + min_p * (prices[i] >= prices[min_p])
        return max_prof



cases = (
    [7,1,5,3,6,4],
    [7,6,4,3,1],
    [2,4,1],
    [3,2,6,5,0,3],
    [2,1,2,0,1],
    [3,3,5,0,0,3,1,4],
)

a = Solution()
b = a.maxProfit

for i in cases:
    print(b(i))
