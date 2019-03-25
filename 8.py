import re
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        group = re.match(r'(([-\+]\d+)|\d+).?', str)
        if group is None:
            return 0
        temp = group.groups()
        temp1 = int(temp[0])
        temp2 = pow(2, 31)
        if temp1 > (temp2 - 1):
            return temp2-1
        elif(temp1 < (-1*temp2)):
            return -1*temp2
        return temp1

##时间：65.29%， 内存：0.90%
