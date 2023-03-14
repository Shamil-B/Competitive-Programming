class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.mappings = []
        self.dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        
        def backtrack(combination,s):
            
            if s=="":
                if combination:
                    self.mappings.append(combination)
                return
            
            candidates = list(self.dic[s[0]])

            for can in candidates:
                
                combination += can
                backtrack(combination,s[1:])
                combination = combination[:-1]
                
        backtrack("",digits)
        return self.mappings