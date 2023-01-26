class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        ptr1 = 0
        ptr2 = len(people)-1

        while ptr1<=ptr2:

            if people[ptr1]+people[ptr2] <= limit and ptr1!=ptr2:
                
                boats+=1
                ptr1+=1
                ptr2-=1

            else:
                
                if people[ptr1] == limit:
                    ptr1+=1
                    
                else:
                    ptr2 -= 1
                    
                boats+=1
                

        return boats