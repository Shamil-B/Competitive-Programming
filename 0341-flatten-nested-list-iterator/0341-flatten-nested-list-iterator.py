# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        st = str(nestedList)
        self.list = []
        self.index = 0
        i = 0
        while i < len(st):
            num = ""
            while (ord(st[i]) > 47 and ord(st[i]) < 58) or st[i] == "-":
                num += st[i]
                i += 1
                
            if num and not (len(num) == 1 and num[0] == "-"):
                self.list.append(int(num))
                
            i += 1
    
    def next(self) -> int:
        current_index = self.index
        self.index += 1
        return self.list[current_index]
    
    def hasNext(self) -> bool:
         return self.index < len(self.list)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())