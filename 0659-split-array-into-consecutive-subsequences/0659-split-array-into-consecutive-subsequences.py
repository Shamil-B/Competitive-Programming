class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        subsequences = []
        
        for num in nums:
            while subsequences and subsequences[0][0] + 1 < num:
                subsequence = heapq.heappop(subsequences)
                if subsequence[1] < 3:
                    return False

            if not subsequences or subsequences[0][0] == num:
                heapq.heappush(subsequences, [num, 1])

            else:
                subsequence = heapq.heappop(subsequences)
                subsequence[0] += 1
                subsequence[1] += 1
                heapq.heappush(subsequences, subsequence)
                
        while subsequences:
            subsequence = heapq.heappop(subsequences)
            if subsequence[1] < 3:
                return False

        return True