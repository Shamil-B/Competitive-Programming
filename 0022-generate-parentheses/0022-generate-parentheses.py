class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        tmpArr = []

        def helper(p,cl):

            if p == cl == n:
                res.append("".join(tmpArr))
                return

            if p < n:
                tmpArr.append('(')
                helper(p+1,cl)
                tmpArr.pop()

            if cl < p:
                tmpArr.append(')')
                helper(p,cl+1)
                tmpArr.pop()

        helper(0,0)
        return res