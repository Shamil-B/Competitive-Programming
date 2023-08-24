class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        ind = 0
        curWord = []
        curWidth = 0
        while ind < len(words):
            curWidth = len("".join(curWord))
            if curWidth + len(words[ind]) + 1 > maxWidth :
                totalSpaces = maxWidth - curWidth
                if len(curWord) == 1:
                    curWord += " " * totalSpaces

                else:
                    if len(words[ind]) == maxWidth:
                        curWord.append(words[ind])
                        ind += 1

                    else:
                        i = 0
                        while totalSpaces > 0:
                            curWord[i] += " "
                            i = (i+1)%(len(curWord)-1)
                            totalSpaces -= 1

                ans.append("".join(curWord))
                curWord = []

            elif curWidth + len(words[ind]) + 1 == maxWidth:
                if len(curWord) == 0:
                    ans.append(words[ind]+" ")
                else:
                    ans.append("".join(curWord) + " " + words[ind])
                ind += 1
                curWord = []
                
            else:
                if curWidth != 0:
                    curWord += [" " + words[ind]]
                else:
                    curWord += [words[ind]]
                
                ind += 1
                if ind == len(words):
                    if curWidth == 0:
                        ans.append(words[-1] + " "*(maxWidth-len(words[-1])))

                    else:
                        curWidth += 1 + len(words[-1])
                        ans.append("".join(curWord)+" "*(maxWidth-curWidth))

      
        return ans
                