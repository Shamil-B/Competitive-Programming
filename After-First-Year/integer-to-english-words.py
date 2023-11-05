class Solution:
    def numberToWords(self, num: int,m=0,old_size=0) -> str:
        res = self.toString(num)
        return self.check(res)

    def toString(self,num,m=0):
        m+=1
        dic_1 = {
        0:"",
        1:"One",
        2:"Two",
        3:"Three",
        4:"Four",
        5:"Five",
        6:"Six",
        7:"Seven",
        8:"Eight",
        9:"Nine"
    }

        dic_2 = {
            10:"Ten",
            11:"Eleven",
            12:"Twelve",
            13:"Thirteen",
            14:"Fourteen",
            15:"Fifteen",
            16:"Sixteen",
            17:"Seventeen",
            18:"Eighteen",
            19:"Nineteen"
        }

        dic_3 = {
            3:"Hundred",
            4:"Thousand",
            5:"Thousand",
            6:"Thousand",
            7:"Million",
            8:"Million",
            9:"Million",
            10:"Billion",
            11:"Billion",
            12:"Billion"
        }
        dic_10 = {
            2 : "Twenty",
            3 : "Thirty",
            4 : "Forty",
            5 : "Fifty",
            6 : "Sixty",
            7 : "Seventy",
            8 : "Eighty",
            9 : "Ninety"
        
        }

        size = len(str(num))
        if num==0 and m==1:
            return "Zero"

        if len(str(num))==0:
            return ""
        if len(str(num))==1:
            return dic_1[num]

        elif (len(str(num)))==2 and str(num)[0]=="1":
            return dic_2[num] 

        elif len(str(num))==2 and str(num)[0]!="1":
            if str(num)[-1]!="0":
                return dic_10[int(str(num)[0])] + self.toString(int(str(num)[1:]),m)
            else:
                return dic_10[int(str(num)[0])] +self.toString(int(str(num)[1:]),m)

        elif len(str(num))==3:

            return dic_1[int(str(num)[0])] + dic_3[len(str(num))]+ self.toString(int(str(num)[1:]),m)

    
        if len(str(num))>3:
            end = size%3
            if end==0:
                end=3
            if str(num)[end]=="0" and len(str(num)[:end])>2:
                return self.toString(int(str(num)[:end]),m) + dic_3[len(str(num))] + self.toString(int(str(num)[end:]),m)
            return self.toString(int(str(num)[:end]),m) + dic_3[len(str(num))] + self.toString(int(str(num)[end:]),m)

    def check(self,res):
        new = res[0]
        for i in range(1,len(res)):

            if ord(res[i])<97:
                new += " "+res[i]

            else:
                new += res[i]

        while new[0]==" ":
            new = new[1:]
        while new[-1]==" ":
            new = new[:-1]

        if new[-4:]=="Zero" and len(new)>4:
            new = new[:-5]

        return new
