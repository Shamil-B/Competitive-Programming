class Solution:
    def minOperations(self, logs: List[str]) -> int:
        length = 0
        for log in logs:
            if log[:3]=="../":
                if length:
                    length -= 1

            elif log[0] != ".":
                length += 1
                
        return length