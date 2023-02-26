class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        nums1Set = set(nums1)
        dic = {}
        
        for j in range(len(nums2)):
            while stack and nums2[j] > stack[-1]:
                dic[stack[-1]] = nums2[j]
                stack.pop()
                
            stack.append(nums2[j])
            
        for num in nums1:
            if num in dic:
                res.append(dic[num])
                
            else:
                res.append(-1)
                
        return res