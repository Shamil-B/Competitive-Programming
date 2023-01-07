class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        size = len(boxes)
        minOps = [0 for i in range(size)]
        summ = 0
        
        tmp = minOps.copy()
        
        
        #going forward
        for i in range(size):
            if i>0:
                minOps[i] = minOps[i-1] + summ
            
            if boxes[i] == '1':
                summ += 1
                

        #going backward
        summ = 0
        for i in range(size-1,-1,-1):
            if i < size-1:
                tmp[i] = tmp[i+1] + summ
            
            if boxes[i] == '1':
                summ += 1
                
        for i in range(size):
            minOps[i] += tmp[i]
            
    
                    
        return minOps