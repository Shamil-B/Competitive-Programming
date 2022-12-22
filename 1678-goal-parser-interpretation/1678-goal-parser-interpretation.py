class Solution:
    def interpret(self, command: str) -> str:
        
        ind = 0
        result = ''
        
        while ind < len(command):
            
            if command[ind] == 'G':
                result += 'G'
                ind+=1
                
            elif command[ind] == '(' and command[ind+1]==')':
                result += 'o'
                ind += 2
                
            else:
                result += 'al'
                ind += 4
                
        return result