class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
                res.append(self.maxx(nums2[nums2.index(nums1[i]):]))
                
        return res
        
    def maxx(self,ls):
        if len(ls)==0:
            return -1
        max = ls[0]
        for i in ls:
            if i>max:
                return i
        return -1

