class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        nums = "123456789"
        for i in range(2, 10):
            for j in range(9-i+1):
                ans.append(int(nums[j:j+i]))

        ans.sort()
        start = bisect_left(ans, low)
        end = bisect_right(ans, high)
        return ans[start:end]