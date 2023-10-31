class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        size = len(nums)
        def backtrack(arr, path):
            if len(path) >= size:
                self.ans.append(path)
                return

            used = []
            for i in range(len(arr)):
                if arr[i] not in used:
                    used.append(arr[i])
                    new_arr = arr[:]
                    new_arr.remove(arr[i])
                    backtrack(new_arr, path[:]+[arr[i]])
                
        backtrack(nums[:], [])
        return self.ans