class Solution:
    def minSteps(self, n: int) -> int:
        arr = [0]*(n+1)
        if(n==1): 
            return 0
        arr[1] = 0
        if(n==2): 
            return 2
        arr[2] = 2

        for i in range(3,n+1):
            max_ = 1 if(i%2!=0) else 2

            if(max_!=2):
                for j in range(3,n//2,2):
                    if(i%j==0):
                        max_ = j
                        break
            arr[i] = arr[i//max_]+max_ if max_!=1 else i
        return arr[n]