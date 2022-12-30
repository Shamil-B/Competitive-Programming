class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        result = []
        sum1 = 0
        dic = {}     #to collect nums elements evenness
        
        for ind,num in enumerate(nums):
            
            if num%2==0:
                sum1 += num
                dic[ind] = True
                
            else:
                dic[ind] = False
        
        
        for i in range(len(nums)):
            
            index = queries[i][1]
            val = queries[i][0]
            oldVal = nums[index]
            nums[index] += val
            newVal = nums[index]

            
            if (newVal)%2 == 0:
            
                if dic[index]:
                    sum1 = sum1 - oldVal + newVal
                
                else:
                    sum1 += newVal
                    
                dic[index] = True
                
            else:
                if dic[index]:
                    sum1 = sum1 - oldVal
                    
                dic[index] = False

            result.append(sum1)
            
            
        return result
            
    
    
        