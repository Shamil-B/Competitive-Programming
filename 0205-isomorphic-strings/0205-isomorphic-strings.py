class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        arr1 = []
        arr2 = []
        counter = 1
        
        for ch in s:
            if ch in dic:
                arr1.append(dic[ch])
                
            else:
                dic[ch] = counter
                counter += 1
                arr1.append(dic[ch])
                
        counter = 1
        dic = {}
        for ch in t:
            if ch in dic:
                arr2.append(dic[ch])
                
            else:
                dic[ch] = counter
                counter += 1
                arr2.append(dic[ch])
                
        return arr1 == arr2
                
