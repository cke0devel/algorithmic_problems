# difficulty: Easy
# Runtime: 73 ms, faster than 55.78% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
# Memory Usage: 14 MB, less than 71.93% of Python3 online submissions for Final Prices With a Special Discount in a Shop.

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = [0] * len(prices)

        for i in range(len(prices)):
            cost = prices[i]

            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    cost -= prices[j]
                    break

            ans[i] = cost

        return ans

