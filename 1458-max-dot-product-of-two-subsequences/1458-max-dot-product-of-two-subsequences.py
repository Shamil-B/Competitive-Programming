class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if max(nums1) * max(nums2) < 0 and min(nums1) * min(nums2) < 0:
            return max(max(nums1) * max(nums2), min(nums1) * max(nums2), max(nums1) * min(nums2))

        @cache
        def  solve(ind1, ind2):
            if ind1 >= len(nums1) or ind2 >= len(nums2):
                return 0

            # choose both
            both = solve(ind1+1, ind2+1) + (nums1[ind1] * nums2[ind2])
            # choose first
            first = solve(ind1, ind2+1)
            # choose second
            second = solve(ind1+1, ind2)
            # choose neither

            return max(both, first, second)

        return solve(0,0)