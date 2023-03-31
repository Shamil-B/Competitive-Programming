class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        allOnes = pow(2,int(math.log(n,2))+1)-1
        return (n^(n>>1))==allOnes