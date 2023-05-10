#User function Template for python3
from collections import deque

class Solution:
    def findOrder(self,alienDic,N,K):
        graph = {}
        size = len(alienDic)
        nonStarters = set()
        allChars = set()
        for word in alienDic:
            for ch in word:
                allChars.add(ch)

        for idx in range(size-1):
            res = self.processWords(alienDic[idx],alienDic[idx+1])
            if res:
                pre,after = res
                nonStarters.add(after)
                if pre in graph:
                    graph[pre].append(after)

                else:
                    graph[pre] = [after]

        
        starters = []
        for key in graph.keys():
            if key not in nonStarters:
                starters.append(key)

        result =  self.topologicalSort(graph,starters)
        allChars = list(allChars)
        setResult = set(result)
        for ch in allChars:
            if ch not in setResult:
                result.append(ch)

        return result


    def processWords(self,word1,word2):
        p1 = 0
        p2 = 0
        n = len(word1)
        m = len(word2)

        while p1<n and p2<m and word1[p1]==word2[p2]:
            p1 += 1
            p2 += 1

        if p1<n and p2<m and word1[p1]!=word2[p2]:
            return word1[p1],word2[p2]

        return False

    def topologicalSort(self,graph,starters):

        for key in graph.keys():
            graph[key] = list(set(graph[key]))

        q = deque(starters)
        visited = set()
        stack = []
        preReqs = {}

        for pre in graph.keys():
            for node in graph[pre]:
                if node in preReqs:
                    preReqs[node] += 1
                else:
                    preReqs[node] = 1

        while q:
            node = q.popleft()
            stack.append(node)

            if node in graph:
                for neig in graph[node]:
                    preReqs[neig] -= 1

                    if neig not in visited and preReqs[neig]==0:
                        visited.add(neig)
                        q.append(neig)

        return stack
#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends