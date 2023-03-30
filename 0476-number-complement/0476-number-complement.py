class Solution:
    def findComplement(self, num: int) -> int:
        nearestTwoPower = pow(2,int(math.log(num,2))+1)
        return num^(nearestTwoPower-1)