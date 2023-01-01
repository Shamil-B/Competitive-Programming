class Solution:

    # the powers of two
    powers = set([2**i for i in range(22)])

    def countPairs(self, deliciousness: List[int]) -> int:

        # number of occurences
        count = collections.Counter(deliciousness)

        result = 0
        for item, val in count.items():

            if item in self.powers:
                result += val*(val-1)//2
            

            for power in self.powers:
                if power > 2*item:
                    result += count[power - item]*val
                    
        return result%(10**9+7)

                