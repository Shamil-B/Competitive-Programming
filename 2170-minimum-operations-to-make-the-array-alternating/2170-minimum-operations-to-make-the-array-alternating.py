class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        odd_freq = defaultdict(int)
        even_freq = defaultdict(int)
        
        if len(nums) == 1:
            return 0
        
        if len(set(nums)) == 1:
            return len(nums)//2

        for index, num in enumerate(nums):
            if index % 2:
                odd_freq[num] += 1
            else:
                even_freq[num] += 1

        even_items = list(even_freq.items())
        even_items.sort(key = lambda x : x[1])        
        even_max_1 = even_items[-1][0]
        even_max_2 = 0
        if len(even_items) > 1:
            even_max_2 = even_items[-2][0]

        odd_items = list(odd_freq.items())
        odd_items.sort(key = lambda x : x[1])   
        odd_max_1 = odd_items[-1][0]
        odd_max_2 = 0
        if len(odd_items) > 1:
            odd_max_2 = odd_items[-2][0]
            
        if odd_max_1 != even_max_1:
            return len(nums) - (odd_freq[odd_max_1] + even_freq[even_max_1])
        return len(nums) - max(odd_freq[odd_max_1] + even_freq[even_max_2], odd_freq[odd_max_2] + even_freq[even_max_1])