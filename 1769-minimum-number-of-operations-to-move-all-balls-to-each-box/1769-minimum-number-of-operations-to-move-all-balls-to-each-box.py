class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        size = len(boxes)
        minOps = [0 for i in range(size)]
        
        for i in range(size):
            for j in range(size):
                if boxes[j] == '1' and i != j:
                    minOps[i] += abs(j-i)
                    
                    
        return minOps