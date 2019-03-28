class Solution:
    def romanToInt(self, s: str) -> int:
        print(s)
        dict1 = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
        list1 = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        index = 0
        value = 0
        temp = ""
        while index < len(s):
            if (index + 1) < len(s):
                temp = "".join((s[index], s[index+1]))
            if  temp in list1:
                value += dict1[temp]
                index += 2
                temp = ""
            else:
                value += dict1[s[index]]
                index += 1
                
        return value
