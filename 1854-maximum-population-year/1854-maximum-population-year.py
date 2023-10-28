class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population_raw = [0]*101

        for birth_year, death_year in logs:
            population_raw[birth_year-1950] += 1
            population_raw[death_year-1950] -= 1

        population = [population_raw[0]]
        for i in range(1, 101):
            population.append(population[-1]+population_raw[i])

        max_index = 0
        for i in range(101):
            if population[i] > population[max_index]:
                max_index = i
        return 1950 + max_index