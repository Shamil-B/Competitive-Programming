class Trie:
    def __init__(self):
        self.root = {}
 
    def insert(self, num):
        current = self.root
        for bit in num:
            bit = int(bit)
            if bit not in current:
                current[bit] = {}
            current = current[bit]

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        size = len(nums)
        trie = Trie()
        bins = []
        for num in nums:
            binary = bin(num)[2:]
            binary = "0"*(32-len(binary)) + binary
            bins.append(binary)
            
        for binary in bins:
            trie.insert(binary)
            
        maxXor = 0
        for num in nums:
            current = trie.root
            xor = 0
            for i in range(31,-1,-1):
                bit = (num>>i)&1
                if bit^1 in current:
                    xor += (1<<i)
                    current = current[bit^1]
                else:
                    current = current[bit]

            maxXor = max(maxXor, xor)

        return maxXor
                