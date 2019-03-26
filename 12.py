class Solution:
    def intToRoman(self, num: int) -> str:
        list1 = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        dict1 = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L',
                 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        print(num)
        
        roman_number = ""
        while num > 0:
            for i, element in enumerate(list1):
                if num < element:
                    base = i-1
                    break
                else:
                    base = i
            num -= list1[base]
            list1 = list1[:base+1]
            roman_number = "".join((roman_number, dict1[list1[base]]))
            
        return roman_number

##时间：40.21%，内存：0.78%
