class Solution:
    def largestNumber(self,ls):
        new = []
        for i in ls:
            b = False
            for j in new:
                if str(j[0])[0] == str(i)[0]:
                    j.append(i)
                    b = True
                    break

            if not b:
                new.append([i])

        for k in range(len(new)):
            new[k] = self.merge(new[k])


        for l in range(len(new)):
            for n in range(len(new[l])):
                new[l][n] = str(new[l][n])

        new = sorted(new, key=lambda x:x[0][0])
        new = reversed(new)
        res = ""

        for ls in new:
            for item in ls:
                res += str(item)
                
        res = str(int(res))

        return res


    def merge(self,ls):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(ls)-1):
                    if int(str(ls[i])+str(ls[i+1])) < int(str(ls[i+1])+str(ls[i])):
                        ls[i],ls[i+1] = ls[i+1],ls[i]
                        swapped = True
        return ls
