class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        print(strs)
        subfix = ""
        if (len(strs) == 0):
            return subfix
        if len(strs) == 1:
            return strs[0]
        flag = False
        index = 0
        while index < len(strs[0]):
            for element2 in strs[1:]:
                if index >= len(element2):
                    flag = True
                    break
                if strs[0][index] != element2[index]:
                    flag = True
            print(flag)
            if flag is True:
                flag = False
                break
            else:
                subfix = "".join((subfix, strs[0][index]))
            print(subfix)
            index +=1
            
        return subfix
