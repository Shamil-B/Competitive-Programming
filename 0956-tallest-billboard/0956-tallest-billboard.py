class Solution(object):
    def tallestBillboard(self, rods):
        dp = {}; n = len(rods)
        def recurse(sum1, sum2, i):
            if i == n: return sum1 if sum1==sum2 else -1
            diff = abs(sum1-sum2)
            if(dp.get((i, diff))==None):
                m = max([-1, recurse(sum1+rods[i], sum2, i+1), recurse(sum1, sum2+rods[i], i+1), recurse(sum1, sum2, i+1)])
                dp[i, diff] = max(m - max(sum1, sum2), -1)
            return (dp[i, diff] + max(sum1, sum2)) if dp.get((i, diff))!=-1 else -1
        return max(0, recurse(0,0,0))