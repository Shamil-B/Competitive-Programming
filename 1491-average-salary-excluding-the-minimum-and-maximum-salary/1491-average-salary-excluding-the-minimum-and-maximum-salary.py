class Solution:
    def average(self, salary: List[int]) -> float:
        
        minn = salary[0]
        maxx = salary[0]
        summ = 0
        size = len(salary)
        
        
        for i in range(size):
            s = salary[i]
            
            summ += s
            
            if s<minn:
                minn = s
                
            if s>maxx:
                maxx = s
                
        summ = summ - maxx - minn
            
        return summ/(size-2)