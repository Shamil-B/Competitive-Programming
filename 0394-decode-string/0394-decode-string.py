class Solution:
    def decodeString(self, s: str) -> str:
        if len(s)==1 and s[0].isdigit():
            return ""
        dic = {"[":"(","]":")"}
        res = ""
        i = 0
        while i < len(s):
            tmp = i
            if s[i]=="[" or s[i]=="]":
                res+=dic[s[i]]
                if res[-1]==")" and i+1<len(s) and (s[i+1]=="(" or s[i+1].isalpha() or s[i+1].isdigit()):
                        res+="+"



            elif s[i].isdigit():
                num = ""
                b = False
                while s[i].isdigit():
                    num+=s[i]
                    i+=1
                    b = True
                if b:
                    if len(num)-i==0:
                        res += num+"*"
                    elif s[i-1]=="+":
                        res += num+"*"
                    else:
                        res += "+" + num+"*"

                else:
                    if i==0:
                        res += s[i]+"*"
                    elif s[i-1]=="+":
                        res += s[i]+"*"
                    else:
                        res += "+" + s[i]+"*"

            elif s[i].isalpha():
                res+='"'
                while i<len(s) and s[i].isalpha():
                    res+=s[i]
                    i += 1
                res += '"'
            else:
                res+=s[i]

            if tmp==i:
                i+=1

        return eval(res)

