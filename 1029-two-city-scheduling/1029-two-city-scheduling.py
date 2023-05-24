class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = []
        n = len(costs)//2
        for index,item in enumerate(costs):
            arr.append((item[0]-item[1],item))
            
        arr.sort()
        cost = 0
        for index,item in enumerate(arr):
            if index<n:
                cost+=item[1][0]
                
            else:
                cost+=item[1][1]
                
        return cost