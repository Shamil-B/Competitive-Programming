class Solution:
    def candy(self, ratings: List[int]) -> int:
        indices = []
        n = len(ratings)
        candies = {i:0 for i in range(n)}

        for index, num in enumerate(ratings):
            indices.append((num,index))

        indices.sort()

        for i in range(n):
            ind = indices[i][1]
            left = right = 0

            if ind > 0 and ratings[ind] > ratings[ind-1]:
                left = candies[ind-1]
                
            if ind < n-1 and ratings[ind] > ratings[ind+1]:
                right = candies[ind+1]
             
            candies[ind] += max(left, right) + 1
            
        return sum(list(candies.values()))