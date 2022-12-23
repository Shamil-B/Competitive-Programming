class Solution:
    def average(self, salary: List[int]) -> float:
        
        minn = salary[0]
        maxx = salary[0]
        summ = 0
        
        
        for i in range(len(salary)):
            s = salary[i]
            
            summ += s
            
            if s<minn:
                minn = s
                
            if s>maxx:
                maxx = s
                
        summ = summ - maxx - minn
            
        return summ/(len(salary)-2)