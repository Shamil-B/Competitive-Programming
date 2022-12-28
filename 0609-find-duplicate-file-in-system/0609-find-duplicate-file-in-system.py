class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        dic = {}
        
        for path in paths:
            path = path.split(' ')  
            dirc = path[0]
            for i in range(1,len(path)):
                indOfContentStart = path[i].index('(')
                content = path[i][indOfContentStart:-1]   #content of the file
                if content in dic:
                    fileName = path[i][:indOfContentStart]
                    dic[content].append(dirc+'/'+fileName)

                else:
                    fileName = path[i][:indOfContentStart]
                    dic[content] = [dirc+'/'+fileName]
                        
        result = []
        
        keys = list(dic.keys())
        
        for key in keys:
            item = dic[key]
            if len(item)>1:
                result.append(item)
                
                
        return result
        
        