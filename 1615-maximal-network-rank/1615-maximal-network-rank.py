class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        neighbours = {}
        maximalNetRank = 0
        for road in roads:
            if road[0] not in neighbours:
                neighbours[road[0]] = [road[1]]

            else:
                neighbours[road[0]].append(road[1])

            if road[1] not in neighbours:
                neighbours[road[1]] = [road[0]]

            else:
                neighbours[road[1]].append(road[0])

        nodes = list(neighbours.keys())
        for node1 in nodes:
            for node2 in nodes:
                if node1!=node2:
                    if node1 in neighbours[node2]:
                        sum_ = len(neighbours[node1])+len(neighbours[node2])-1
                        
                    else:
                        sum_ = len(neighbours[node1])+len(neighbours[node2])
                    maximalNetRank = max(maximalNetRank,sum_)

        return maximalNetRank