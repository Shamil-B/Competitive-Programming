class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue == target:
            return 0

        @cache
        def solve(curVal):
            if curVal == startValue:
                return 0

            # Two options
            # 1. divide
            div = add = inf
            if curVal > startValue:
                if curVal%2:
                    div = solve(curVal+1)
                else:
                    div = solve(curVal//2)

            # 2. add one
            if curVal < startValue:
                add = startValue-curVal-1

            return min(div,add) + 1
        return solve(target)