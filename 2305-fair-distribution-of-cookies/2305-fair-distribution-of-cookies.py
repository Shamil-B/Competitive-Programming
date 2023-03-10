class Solution:
    def distributeCookies(self, cookies,k):
        self.kids = [0]*k
        self.max = float("inf")
        self.total = sum(cookies)
        self.cookies = cookies
        self.cookies.sort(reverse=True)
        
        def backtrack(curCookieIdx):
            
            if sum(self.kids) == self.total:
                self.max = min(max(self.kids),self.max)
                return
            
            if max(self.kids) > self.max:
                return
            
            for i in range(len(self.kids)):
                self.kids[i] += self.cookies[curCookieIdx]
                backtrack(curCookieIdx+1)
                self.kids[i] -= self.cookies[curCookieIdx]
                
            
        backtrack(0)
        return self.max