class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        
        for item in cpdomains:
            splitted = item.split(' ')
            
            num = int(splitted[0])
            dom = splitted[1]
            
            doms = self.splitter(dom)
            
            for item in doms:
                if item not in dic:
                    dic[item] = num
                    
                else:
                    dic[item] += num
                    
        result = []
        
        keys = list(dic.keys())
        
        for key in keys:
            result.append(str(dic[key])+" "+key)
                          
        return result
        
        
    def splitter(self,dom):
        res = [dom]
        
        for i in range(len(dom)):
            if dom[i]=='.':
                res.append(dom[i+1:])
                
        return res