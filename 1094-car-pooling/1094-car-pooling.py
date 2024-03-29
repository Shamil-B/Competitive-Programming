class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        psg = 0
        n = len(trips)
        dic = {}
        arr = []

        trips = sorted(trips,key=lambda x:x[1])
        if n==1 and capacity<trips[0][0]:
            return False

        for i in range(n):
            arr.sort()
            arr.reverse()
            while arr and arr[-1]<=trips[i][1]:
                psg-=dic[arr[-1]]
                arr.pop()
            if trips[i][2] not in arr:
                arr.append(trips[i][2])
            if trips[i][2] not in dic:
                dic[trips[i][2]] = trips[i][0]
            else:
                dic[trips[i][2]] += trips[i][0]
            psg+=trips[i][0]
            if psg>capacity:
                return False
                
        return True