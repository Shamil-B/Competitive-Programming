class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        newGraph = {-1:[]}
        childs = set()
        for i in range(n):
            newGraph[i] = [leftChild[i], rightChild[i]]
            childs.add(leftChild[i])
            childs.add(rightChild[i])
            
        root = 0
        for i in range(n):
            if i not in childs:
                root = i

        visited = set()
        def validate(node,visited):
            if node == -1:
                return True

            if node in visited:
                return False
            
            visited.add(node)
            left = newGraph[node][0]
            right = newGraph[node][1]

            if node in newGraph[left] or node in newGraph[right]:
                return False

            leftRes = validate(left,visited)
            rightRes = validate(right,visited)
            
            return leftRes and rightRes
        return validate(root,visited) and len(visited) == n