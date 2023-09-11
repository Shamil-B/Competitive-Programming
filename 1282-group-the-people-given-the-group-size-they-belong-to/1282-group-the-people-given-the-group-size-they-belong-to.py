class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        dic = defaultdict(list)
        n = len(groupSizes)
        for i in range(n):
            dic[groupSizes[i]].append(i)
            
        ans = []
        for size, people in dic.items():
            start = 0
            for end in range(size,len(people)+1,size):
                ans.append(people[start:end])
                start = end
            
        return ans