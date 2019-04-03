class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_list = []
        if s == "":
            len_list.append(0)
            return 0
        s1 = list(s)
        for i, element1 in enumerate(s1):
            temp = "".join((element1))
            len_list.append(len(temp))
            for _, element2 in enumerate(s1[i+1:]):
                if element2  not in temp:
                    temp = "".join((temp, element2)) 
                    ###这一句改成temp = temp.join((element2))会报错
                else:
                    break
            len_list.append(len(temp))
        return max(len_list)
