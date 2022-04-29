# difficulty: Easy
# Runtime: 43 ms, faster than 88.07% of Python3 online submissions for Fizz Buzz.
# Memory Usage: 15.2 MB, less than 5.19% of Python3 online submissions for Fizz Buzz.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []

        for i in range(1,n+1):
            s = ''

            if i%3==0:
                s += 'Fizz'
            if i%5==0:
                s += 'Buzz'

            if i%3>0 and i%5>0:
                s = str(i)

            ans.append(s)

        return ans
