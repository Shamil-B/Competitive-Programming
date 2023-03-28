class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = []
        right = []
        n = len(fruits)
        max_ = 0
        initialFruit = 0

        for item in fruits:
            pos = item[0]
            if abs(pos-startPos)>max_:
                max_ = abs(pos-startPos)
                
        max_ = max(max_,k)

        left = [0]*max_
        right = [0]*max_

        for item in fruits:
            pos = item[0]
            amt = item[1]
            if pos==startPos:
                initialFruit = amt

            elif pos<startPos:
                left[startPos-pos-1] = amt
                
            else:
                right[pos-startPos-1] = amt
                
        if k==0:
            return initialFruit
                
        #axis constructed in a beautiful way now to the real work
        
        #first we do the prefixsum for both
        
        for i in range(1,len(left)):
            left[i] += left[i-1]
            
        for i in range(1,len(right)):
            right[i] += right[i-1]
            
        #first all the way k to left and k to right
        runningMax = max(left[k-1],right[k-1])

        #now we check back and forthes starting from n where n is (k-1)//2 for a mystrious reason

        n = (k-1)//2

        while n>0:
            runningMax = max(runningMax,left[n-1]+right[k-2*n-1])
            n -= 1
            
        n = (k-1)//2

        while n>0:
            runningMax = max(runningMax,right[n-1]+left[k-2*n-1])
            n -= 1
            
        return runningMax+initialFruit