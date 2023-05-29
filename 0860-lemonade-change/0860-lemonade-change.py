class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        total = 0
        myBills = {5:0,10:0}
        for bill in bills:
            if bill == 10:
                if myBills[5]<1:
                    return False
                myBills[5] -= 1
                myBills[10] += 1
                
            elif bill==20:
                if myBills[5]<1 or total<15:
                    return False
                
                if myBills[10]>0:
                    myBills[10] -= 1

                else:
                    myBills[5] -= 2
                    if myBills[5]<1 or total<15:
                        return False

                myBills[5]-=1

                
            else:
                myBills[5] += 1
                
            total += 5
            
        return True
                