class Solution:
    def longestPalindrome(self, s: str, start: int, end: int ) -> str:
        #------------第一种解法：暴力解法--------------------------
        #maxLen = 0
        #str_list = []
        #print(s)
        #if s=="":
        #    return s
        #str_list.append(s[0])
        #for i, element1 in enumerate(s):
        #    if maxLen > (len(s)-i):
        #        break
        #    temp = [element1]
        #    for j, element2 in enumerate(s[i+1:]):
        #        temp.append(element2)
        #        if temp[::] == temp[::-1]:
        #            temp2 = "".join(temp)
        #            str_list.append(temp2)
        #            if len(temp2) > maxLen:
        #                maxLen = len(temp2)
        #count_list = [len(i) for i in str_list]           
        #index = count_list.index(max(count_list))
        #return str_list[index]
        #----------------------------------------------------------
        #---------------第二种--------------------------------------
        #outString = ""
        #while len(s) > len(outString):
        #    indLen = len(outString)
        #    temp = s[: indLen]
        #    for ch in s[indLen:]:
        #        temp += ch
        #        if temp == temp[::-1]:
        #            outString = temp if  len(temp)>len(outString) else outString
        #    s = s[1:]
        #return outString            
        #--------------------------------------------------------------
