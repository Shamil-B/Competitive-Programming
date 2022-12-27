class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs[0] == '':
            return ''
        
        cmn = strs[0][0]

        for string in strs:
            if not string.startswith(cmn):
                return ""

        if len(strs)==1:
            return cmn

        ind = 1

        while ind < len(strs[0]):
            cmn += strs[0][ind]
            for string in strs:
                if not string.startswith(cmn):
                    return cmn[:-1]
            ind += 1

        return cmn