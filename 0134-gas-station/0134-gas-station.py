class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        size = len(gas)
        netGas = [0]*size

        for i in range(size):
            netGas[i] = gas[i] - cost[i]

        pfs = [netGas[-1]]
        for i in range(size-2,-1,-1):
            pfs.append(pfs[-1] + netGas[i])

        pfs.reverse()
        if pfs[0] < 0:
            return -1

        maxInd = 0
        for i in range(size):
            if pfs[i] > pfs[maxInd]:
                maxInd = i

        return maxInd