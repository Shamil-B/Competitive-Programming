class Solution:
    def find132pattern(self, nums) -> bool:
        minn = nums[0]
        maxx = nums[0]
        
        stack = [[nums[0],nums[0]]]
        
        for num in nums:
            
            for i in range(len(stack)-1,-1,-1):
                
                tp = stack[i]
                if num<=tp[0]:
                    break
                    
                if num>tp[0] and num<tp[1]:
                    return True
                
            if stack and num < stack[-1][0]:
                stack.append([num,num])
                
            if num>stack[-1][1]:
                minn = stack[-1][0]
                while stack and num > stack[-1][1]:
                    stack.pop()
                
                stack.append([minn,num])

            
                    
        return False