class Solution:
    def __init__(self):
        self.closed = True


    def removeComments(self, source):
        result = []
        lastOpenLine = []
        ind = 0
        tup = None                   #To make sure we dont use one '/' twice
        block = False
        
        while ind < len(source):

            line = source[ind]
            
            if self.closed:
                newLine = ''
                tup = None
                
                for i in range(len(line)):
                    if line[i] == '/' and i+1<len(line) and line[i+1] == '*':
                        self.closed = False
                        newLine = line[:i]
                        lastOpenLine = newLine
                        ind -= 1
                        tup = (line,i)
                        block = True
                        break
                        
                    elif line[i] == '/' and i+1<len(line) and line[i+1] == '/':
                            newLine = line[:i]
                            i-=1
                            block = False

                            break
                            
                if newLine=='' and not block:
                    newLine = line[:i+1]

                if len(newLine)>0 and not block:
                    result.append(newLine)


                if newLine=='' and self.closed and block:
                    newLine = line[:i+1]

                if len(newLine)>0 and len(lastOpenLine)==0 and block:
                    result.append(newLine)
                    
                ind += 1

            else:
                newLine = ''
                for i in range(len(line)):
                    if line[i] == '*' and i+1<len(line) and line[i+1] == '/' and (tup[0]!=line or tup[1]+1<i):
                        self.closed = True
                        if i+2<len(line):
                            newLine = line[i+2:]
                        break

                if self.closed:
                    lastOpenLine += newLine
                    source[ind] = lastOpenLine

                    if len(lastOpenLine)>0:
                        lastOpenLine = []
                        
                else:
                    ind += 1

        return result