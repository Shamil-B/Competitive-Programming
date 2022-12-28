class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        dic = {}
        
        for path in paths:
            path = path.split(' ')  
            dirc = path[0]
            for i in range(1,len(path)):
                ind1 = path[i].index('(')
                content = path[i][ind1:-1]   #content of the file
                if content in dic:
                    fileName = path[i][:ind1]
                    dic[content].append(dirc+'/'+fileName)

                else:
                    fileName = path[i][:ind1]
                    dic[content] = [dirc+'/'+fileName]
                        
        result = []
        
        keys = list(dic.keys())
        
        for key in keys:
            item = dic[key]
            if len(item)>1:
                result.append(item)
                
                
        return result
        
        