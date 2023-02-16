class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        arr1 = []
        arr2 = []
        counter = 1
        
        for ch in s:
            if ch in dic1:
                arr1.append(dic1[ch])
                
            else:
                dic1[ch] = counter
                counter += 1
                arr1.append(dic1[ch])
                
        counter = 1
        
        for ch in t:
            if ch in dic2:
                arr2.append(dic2[ch])
                
            else:
                dic2[ch] = counter
                counter += 1
                arr2.append(dic2[ch])
                
        return arr1 == arr2
                
