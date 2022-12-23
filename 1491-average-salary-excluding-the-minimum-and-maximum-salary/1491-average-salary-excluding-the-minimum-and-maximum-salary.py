class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop(0)
        salary.pop()
        
        ave = 0
        summ = 0
        
        for s in salary:
            summ += s
            
        return summ/len(salary)