class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        stack = []
        result = 0
        arr = [-inf] + arr + [-inf]
        
        for index, num in enumerate(arr):

            while stack and arr[stack[-1]] > num:
                cur = stack.pop()
                result += arr[cur] * (index - cur) * (cur - stack[-1])

            stack.append(index)
        return result % (10**9 + 7)
