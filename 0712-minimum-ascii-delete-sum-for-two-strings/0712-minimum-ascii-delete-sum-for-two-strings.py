class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        size_1 = len(s1)
        size_2 = len(s2)

        @cache
        def solve(ind_1, ind_2):
            if ind_1 >= size_1:
                sum_ = 0
                for ind in range(ind_2, size_2):
                    sum_ += ord(s2[ind])
                    
                return sum_
            
            if ind_2 >= size_2:
                sum_ = 0
                for ind in range(ind_1, size_1):
                    sum_ += ord(s1[ind])
                    
                return sum_
            
            if s1[ind_1] == s2[ind_2]:
                return solve(ind_1 + 1, ind_2 + 1)
            
            delete_first = solve(ind_1 + 1, ind_2) + ord(s1[ind_1])
            delete_second = solve(ind_1, ind_2 + 1) + ord(s2[ind_2])

            return min(delete_first, delete_second)
        
        return solve(0, 0)