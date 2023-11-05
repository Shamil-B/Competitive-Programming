class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses = {}
        wins = {}
        noLoses = []
        oneLose = []
        
        for match in matches:
            if match[1] in loses:
                loses[match[1]] += 1
                
            else:
                loses[match[1]] = 1
                      
            if match[0] in wins:
                wins[match[0]] += 1
                
            else:
                wins[match[0]] = 1
                     
                     
        for match in matches:
            if match[0] not in loses:
                noLoses.append(match[0])
                     
            elif loses[match[0]] == 1:
                     oneLose.append(match[0])
                    
            if loses[match[1]] == 1:
                     oneLose.append(match[1])
                     
        print(loses)  
        ans1 = list(set(noLoses))
        ans2 = list(set(oneLose))
        ans1.sort()
        ans2.sort()
        return [ans1,ans2]
                     
        
                     
                     
        