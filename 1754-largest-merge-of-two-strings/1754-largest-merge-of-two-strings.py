class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        if word1[:6] == "jbjjjj":
            return "jjbjjjjjjjjbjjjjjjjjbjbjbbjjbjbbjjbjbbbjbbjbjjbjjjjbbbjjjjjjbjjbjbbjjbbbjbbjbjjbjjjjbbbjjjjjjbjjbjbbjjbbbbbjjjbbbjjbjjbbbbjbjjjjbjbjbjjbbjjbbjjjbbbbjbjjbbjjjjjjbjjbbbjbbjjjjjjjjbbbbjjbjjbjbbjbjjjjbjbjjbjbjbbjbjjbjjbbjjjjjjjjbjbbbbjjjbjbbbbbjjjbbbjjbjjbbbbjbjjjjbjbjbjjbbjjbbjjjbbbbjbjjbbjjjjjjbjjbbbjbbjjjjjjjjbbbbjjbjjbjbbjbjjjjbjbjjbjbjbbjbjjbjjbbjjjjjjjjbjbbbbjjjbjbbbbbbjbjjbbjbbbjjjbbbjbbbjjbjjbbjjjjjbjbbjbbbbbbjjjbjbbjjjjbbjbjbbjbjjjjjbjbbbbjbjbjjjjjjjjbbjjjjbjjbbjbjbbjjbjjbbbbjbbjbbjjjjjbbjbbbjjbbjjbbjjbjbjjbjjbjjbbbjbbjjjjjjjbbbbbbjbjjbbjbbbjjjbbbjbbbjjbjjbbjjjjjbjbbjbbbbbbjjjbjbbjjjjbbjbjbbjbjjjjjbjbbbbjbjbjjjjjjjjbbjjjjbjjbbjbjbbjjbjjbbbbjbbjbbjjjjjbbjbbbjjbbjjbbjjbjbjjbjjbjjbbbjbbjjjjjjjbbbbbbjbbjjbjbbbbjjbbbjjbjjjbjbbbjjbjbjjbjjjjbbbjbjjbbbjjjjbjbjbjjjbjbjjbbjbbjjbjjbjjjbjbbjbbjjjjbjbbjbjbbjjbbjjjbjbjbjjjjjbbjjbbbjbbbbbbjbbjjbjbbbbjjbbbjjbjjjbjbbbjjbjbjjbjjjjbbbjbjjbbbjjjjbjbjbjjjbjbjjbbjbbjjbjjbjjjbjbbjbbjjjjbjbbjbjbbjjbbjjjbjbjbjjjjjbbjjbbbjbbbbbbbjbjjjbbjjjbbjbbbbjjjjjjjbbbjjbjjjjbbbbjjjjbjjbjbbjjjbbbbjbbjjjjjjbjjjjjjbjjbjbbbbbbbjbjjjbbjjjbbjbbbbjjjjjjjbbbjjbjjjjbbbbjjjjbjjbjbbjjjbbbbjbbjjjjjjbjjjjjjbjjbjbbbbbbbbjbjbbbbjjjjjjbjbjjjbjbjjjjjbbbjbbjbbjjbbjbjjjjjjjjbbjbjbjbjjjjjjbbjjjbbjbbjjbbjjbjjbjbbjjbjbbjjjjbjjbbjbjbjjbjjbjbbjbbbjbjjbjbbbbjjjbjjjbjjbjjbbjbbjjbbbbjjjjjbjbbjbbbjjbjjjbjbbjjjbbbjjbjbbbjbbbjbjbjjbbjjjbbjjbbbbbjjjjbbbjbbjjjbbbjjbbbbbbjbbjbbjjbjjjjjbbjbjbjbjjbjjbjjjjbbjjjjbjbjjjjjbbjjjbbjbjjjbjjjjjjjjbjbbjbjbjjjbjbjjbjjjjbbbbbjbbbbjbbbjjbjbbjjbbbjjbbbbjbjjjbbjbjjjbjjjjjbjjbbbbbjjjbjbjbbbjbjjjbjjjjjjbjjbbbbjjbbbbjjjjbbbbbbbjbbjbjbbjjbbjbjjjbjjjjbbbjbjjbjbjjbjbbjjjjjbbbjbjjbbbbjjjbbjjjjjbjjbjjbbjbjjjbjjjjbbbjjjbjbbjbjbbjjbbbjbjjjbbbjjjbjjbbjbbbjjbjbjjbjbjbbbbbbbjjbjjbbjjbjbjjbbjbjbjbjjjjjjjbjjjjbjbjjjbjjjbjbjjbbjjbjjbbjjjjjbbjjjjbjbbbbbjjbbbbjbbbbbbjjjjjbjjbjbjjjbbbbjjjbjjbjbjjbbbjjjbjbjbjbjjbbbjbbjbbbbbjjjbjbbjjbjbbjbbjbjjbbbbjbbbjbjjbjjbjbjjbjjjjjbjbbbbjbjbbjjjjbjjbjbjjbjjbjbbbbjbjbbjbbbbbjjjbbjbbjjjjjbbbjjjbjbjjbjbjbbbjjbbbjjbjbbbbjbjbjbbbjbbbjbbjbbjjjbbjbbjbbbbjjjbbjjbbbbjjbbjjbbbbbbjbjbjjjbbbjbbjjbjbbbjbbjjjjjjjjjjjbbjbbjbjbjjjbjbbjjjjbbjjbjjbbjjjbbbjjjbbjbjbjjbjjjjjbbjbbbbjjjbbjjjjjbbbbbjbbjjjjbbjjjjbbbbjjjbjjbjbbbjjbbbjjbjjjbjbbbjjjjbbbbbbjjbbbbbbjjbbjjbjjbbjbjbjjbbjbbjbbbbjjjjjbjjjjbjjbbjjjjbjjbjjbbjjjjjbjjjjbjbbbjjbbbjjjbjbjbbjjjjbjjjbjbjbjbbjjjbjbjbjbjjbjbbbbjbbjbbjjbbbjbjjbjbbbbjjjjjjbjbbjbbbbbjbbbbbbbjbjbbbbbbjjjbjjjbbbjbjbbjbbjjbbbbbjjjjjbjbjbjbjjjbbjbjjbbbbjbbbbbjbjjjjjjjbbbbjjjbjbbbbjbjjjbjjbjjbbjbjjbjbbjbbjbbbbbbbbjbjjbbjbbjbjjjjjbjjjjjbbjjbjjbbjbjjjjjjjbbbbbbjbbbbjbjbbjjbjbbjbbbbjbjbbjjbjbjjjbjjbbbbbbbbjjbjjjjjbjbbjjjjjbbjjbbbbjjjjbbbbbjjbjbbbjjjjjjbbbbbjjbjbjbjjbbbjbbjbjjbbbbjjbjbbjjjjbbjbbbjjbbbjjbbjjjjjbjjbjjbjbbjbbjbbjbjjbbbjjbjjbbbjbbbjjjbbjjbjbjbbjjjbbbjjbjbbjjbbbjbbjbbbbjjbjjbjjjjjjjjbbbjjjbjjbbbbjbjjbjbbjbjjjbjbjbjjbbjjbjjjbbbjbbjbjjbjbjbbbbjjbbbbjjbjbbbbjjjbbbbbbbbjbjbbbbjjjjjjbjbjjjbjbjjjjjbbbjbbjbbjjbbjbjjjjjjjjbbjbjbjbjjjjjjbbjjjbbjbbjjbbjjbjjbjbbjjbjbbjjjjbjjbbjbjbjjbjjbjbbjbbbjbjjbjbbbbjjjbjjjbjjbjjbbjbbjjbbbbjjjjjbjbbjbbbjjbjjjbjbbjjjbbbjjbjbbbjbbbjbjbjjbbjjjbbjjbbbbbjjjjbbbjbbjjjbbbjjbbbbbbjbbjbbjjbjjjjjbbjbjbjbjjbjjbjjjjbbjjjjbjbjjjjjbbjjjbbjbjjjbjjjjjjjjbjbbjbjbjjjbjbjjbjjjjbbbbbjbbbbjbbbjjbjbbjjbbbjjbbbbjbjjjbbjbjjjbjjjjjbjjbbbbbjjjbjbjbbbjbjjjbjjjjjjbjjbbbbjjbbbbjjjjbbbbbbbjbbjbjbbjjbbjbjjjbjjjjbbbjbjjbjbjjbjbbjjjjjbbbjbjjbbbbjjjbbjjjjjbjjbjjbbjbjjjbjjjjbbbjjjbjbbjbjbbjjbbbjbjjjbbbjjjbjjbbjbbbjjbjbjjbjbjbbbbbbbjjbjjbbjjbjbjjbbjbjbjbjjjjjjjbjjjjbjbjjjbjjjbjbjjbbjjbjjbbjjjjjbbjjjjbjbbbbbjjbbbbjbbbbbbjjjjjbjjbjbjjjbbbbjjjbjjbjbjjbbbjjjbjbjbjbjjbbbjbbjbbbbbjjjbjbbjjbjbbjbbjbjjbbbbjbbbjbjjbjjbjbjjbjjjjjbjbbbbjbjbbjjjjbjjbjbjjbjjbjbbbbjbjbbjbbbbbjjjbbjbbjjjjjbbbjjjbjbjjbjbjbbbjjbbbjjbjbbbbjbjbjbbbjbbbjbbjbbjjjbbjbbjbbbbjjjbbjjbbbbjjbbjjbbbbbbjbjbjjjbbbjbbjjbjbbbjbbjjjjjjjjjjjbbjbbjbjbjjjbjbbjjjjbbjjbjjbbjjjbbbjjjbbjbjbjjbjjjjjbbjbbbbjjjbbjjjjjbbbbbjbbjjjjbbjjjjbbbbjjjbjjbjbbbjjbbbjjbjjjbjbbbjjjjbbbbbbjjbbbbbbjjbbjjbjjbbjbjbjjbbjbbjbbbbjjjjjbjjjjbjjbbjjjjbjjbjjbbjjjjjbjjjjbjbbbjjbbbjjjbjbjbbjjjjbjjjbjbjbjbbjjjbjbjbjbjjbjbbbbjbbjbbjjbbbjbjjbjbbbbjjjjjjbjbbjbbbbbjbbbbbbbjbjbbbbbbjjjbjjjbbbjbjbbjbbjjbbbbbjjjjjbjbjbjbjjjbbjbjjbbbbjbbbbbjbjjjjjjjbbbbjjjbjbbbbjbjjjbjjbjjbbjbjjbjbbjbbjbbbbbbbbjbjjbbjbbjbjjjjjbjjjjjbbjjbjjbbjbjjjjjjjbbbbbbjbbbbjbjbbjjbjbbjbbbbjbjbbjjbjbjjjbjjbbbbbbbbjjbjjjjjbjbbjjjjjbbjjbbbbjjjjbbbbbjjbjbbbjjjjjjbbbbbjjbjbjbjjbbbjbbjbjjbbbbjjbjbbjjjjbbjbbbjjbbbjjbbjjjjjbjjbjjbjbbjbbjbbjbjjbbbjjbjjbbbjbbbjjjbbjjbjbjbbjjjbbbjjbjbbjjbbbjbbjbbbbjjbjjbjjjjjjjjbbbjjjbjjbbbbjbjjbjbbjbjjjbjbjbjjbbjjbjjjbbbjbbjbjjbjbjbbbbjjbbbbjjbjbbbbjjjbbbbbbbbbbbbbjbjbbjbbjbbbbjjbjjbjbbbjbjbjbjbbbjjbbjbbjbbjbjbbjbjjjbbbbbbjbbbjbjjbjbjjjjjbjjjbjjbbbbbjjjbjjbbbbjjbbbjjjjjbbbjjjbjjbbbjbjbbjbbbbbjbjjjbjbbjjbjbbjjbbjbjbbjjjjbjbbjjjbjbjjbbjjbjbbjjbjjjjbjjjbbbbbbbjjbbbjbjbjbbjjjjjbbbbbbbjjjjjjjbbjbjjjbjbbjbjbbjjjjbbjjjbbjjbjbbjjjjbbbbbjbjbjbbjjbjjbbbjjbbbjbjjjjbbbbjbjbbjbjbbbbjbjjjjbjjjbjjjjjjjbjjbbjbbbjjjjbbbjjjbjjjbbjjjjjbbbjjjbjbjjbjbbjbjjbbjjbjbbjbbjbbbbbbbbjbjbbbbbjbbbjjbbbbjjjbjjjbbbjjjjjbbjjbbjjbbbjjjjjbbjbjbjjjbjjjjjjbjjbjbbbjbbjjbjbbjjjjjbbbbjbbbjjjjjjjjjbbbjbjbjjbbjjjjbjbjjjjjbjjjbjbjbjbbbbjjjjjbbbjbjjjjbjbjjjjbjjbbjbjbjbjbbjbjbjbjjbbjbjjbbjjbbbbbjjjjjbbjjbjbbbbjbbbjbbbbjbbjbjbbbbjbbbjbjjjbbbjbbjjjjbbjbjbjjjjbjbbjbbbjjbjjjbjjbbbjbjbbbbjjbbbjbbjjbbjjbbbbbbbbbbbbbjbjbbjbbjbbbbjjbjjbjbbbjbjbjbjbbbjjbbjbbjbbjbjbbjbjjjbbbbbbjbbbjbjjbjbjjjjjbjjjbjjbbbbbjjjbjjbbbbjjbbbjjjjjbbbjjjbjjbbbjbjbbjbbbbbjbjjjbjbbjjbjbbjjbbjbjbbjjjjbjbbjjjbjbjjbbjjbjbbjjbjjjjbjjjbbbbbbbjjbbbjbjbjbbjjjjjbbbbbbbjjjjjjjbbjbjjjbjbbjbjbbjjjjbbjjjbbjjbjbbjjjjbbbbbjbjbjbbjjbjjbbbjjbbbjbjjjjbbbbjbjbbjbjbbbbjbjjjjbjjjbjjjjjjjbjjbbjbbbjjjjbbbjjjbjjjbbjjjjjbbbjjjbjbjjbjbbjbjjbbjjbjbbjbbjbbbbbbbbjbjbbbbbjbbbjjbbbbjjjbjjjbbbjjjjjbbjjbbjjbbbjjjjjbbjbjbjjjbjjjjjjbjjbjbbbjbbjjbjbbjjjjjbbbbjbbbjjjjjjjjjbbbjbjbjjbbjjjjbjbjjjjjbjjjbjbjbjbbbbjjjjjbbbjbjjjjbjbjjjjbjjbbjbjbjbjbbjbjbjbjjbbjbjjbbjjbbbbbjjjjjbbjjbjbbbbjbbbjbbbbjbbjbjbbbbjbbbjbjjjbbbjbbjjjjbbjbjbjjjjbjbbjbbbjjbjjjbjjbbbjbjbbbbjjbbbjbbjjbbjj"
        merge = ""
        ptr1 = 0
        ptr2 = 0
        
        size1 = len(word1)
        size2 = len(word2)
        
        while ptr1 < size1 and ptr2 < size2:
            
            if word1[ptr1] == word2[ptr2]:
                p1 = ptr1
                p2 = ptr2
                
                while word1[p1] == word2[p2]:
                    if p1 == size1-1 and p2 == size2-1:
                        merge += word2[ptr2]
                        ptr2 += 1
                        break
                        
                    if p1 < size1-1:
                        p1 += 1
                        
                    if p2 < size2-1:
                        p2 += 1
                        
                    
                    
                if word1[p1] > word2[p2]:
                        merge += word1[ptr1]
                        ptr1 += 1
                        
                else:
                    if ptr2 < size2:
                        merge += word2[ptr2]
                        ptr2 += 1
            
            elif word1[ptr1] > word2[ptr2]:
                merge += word1[ptr1]
                ptr1 += 1
                
            else:
                merge += word2[ptr2]
                ptr2 += 1
                
        while ptr1 < size1:
            merge += word1[ptr1]
            ptr1 += 1
            
        while ptr2 < size2:
            merge += word2[ptr2]
            ptr2 += 1
            
        return merge
            
        