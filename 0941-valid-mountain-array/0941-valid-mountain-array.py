class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        reversedd = False
        
        if len(arr)<3:
            return False
        
        for i in range(len(arr)-1):
            if not reversedd:
                if arr[i+1] < arr[i]:
                    reversedd = True
                
                elif arr[i+1] == arr[i]:
                    return False
                
                    
            else:
                if arr[i+1] > arr[i] or arr[i+1] == arr[i]:
                    return False
                
        if reversedd and arr[0]<arr[1]:
            return True
        
        return False
        
                
            
      