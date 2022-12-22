class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        temp = x
        newNum = 0


        while temp>0:
            rem = temp%(10)
            temp = temp//10
            newNum = newNum*10 + rem

        if newNum==x:
            return True

        return False
