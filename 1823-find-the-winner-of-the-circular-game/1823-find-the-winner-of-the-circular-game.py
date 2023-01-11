class Solution:
    def findTheWinner(self,n,k,que=[],start=0):
    
        if len(que)==0:
            que=[i for i in range(1,n+1)]
        if len(que)==1:
            return que[0]

        loser = (start+k-1)%len(que)
        que.remove(que[loser])
        start = loser%len(que)

        return self.findTheWinner(n,k,que,start)