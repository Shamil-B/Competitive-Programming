# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {}
        def treeToGraph(root):
            nonlocal graph

            if not root:
                return
            
            if root.left:
                if root.left.val not in graph:
                    graph[root.left.val] = [root.val]
                    
                else:
                    graph[root.left.val].append(root.val)
                    
                if root.val in graph:
                    graph[root.val].append(root.left.val)
                    
                else:
                    graph[root.val] = [root.left.val]
                    
            if root.right:
                if root.right.val not in graph:
                    graph[root.right.val] = [root.val]
                    
                else:
                    graph[root.right.val].append(root.val)
                    
                if root.val in graph:
                    graph[root.val].append(root.right.val)
                    
                else:
                    graph[root.val] = [root.right.val]
                    
            treeToGraph(root.left)
            treeToGraph(root.right)
            
        def bfsWithLimit(graph,target,limit):
            q = deque([(target,0)])
            visited = set()
            elements = []
            level = 0
            
            while q and level<limit+1:
                node,level = q.popleft()
                
                if node in visited:
                    continue
                    
                visited.add(node)
                if level==limit:
                    elements.append(node)

                if node in graph:
                    for neig in graph[node]:
                        q.append((neig,level+1))
                    
            return elements
        
        treeToGraph(root)
        print(graph)
        return bfsWithLimit(graph,target.val,k)