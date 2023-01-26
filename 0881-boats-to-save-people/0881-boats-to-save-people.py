class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        

        while len(people)>0:
            ptr1 = 0
            ptr2 = len(people)-1
            if people[ptr1]+people[ptr2]<=limit and ptr1!=ptr2:
                boats+=1
                people.pop(ptr2)
                people.pop(ptr1)
                continue

            else:
                boats+=1
                people.pop(ptr2)

        return boats