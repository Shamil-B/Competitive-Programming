class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []
        
        for path in paths:
            if path == ".." and stack:
                stack.pop()
                
            elif path!="" and path!="." and path!="..":
                stack.append(path)
                
        newPath = "/".join(stack)
        return "/"+newPath