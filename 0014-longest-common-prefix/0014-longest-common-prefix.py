class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        str=[]
        last=len(strs)-1
        #string builder can be used in java
        for i in range(len(strs[0])):
            if strs[0][i]==strs[last][i]:
                str.append(strs[0][i])
            else : break

        return ''.join(str)
