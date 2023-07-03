class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        query_glass = min(query_glass, query_row - query_glass) # each row is symmetry, row[i] = row[l-i]

        row = [poured]

        for i in range(query_row):

            if query_glass < i/2 and row[query_glass] == 0.0:
                return 0.0

            next_row = [0] * (i + 2)

            for index, champ in enumerate(row):
                q = (champ - 1) / 2
                if q > 0:
                    next_row[index] += q
                    next_row[index + 1] += q
            
            row = next_row
        return min(1.0, row[query_glass])