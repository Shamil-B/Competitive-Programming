class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(list(Counter(arr).values()))) == len(set(arr))