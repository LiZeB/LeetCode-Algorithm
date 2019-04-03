class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = []
        for _, element1 in enumerate(nums1):
            temp.append(element1)
        for _ , element2 in enumerate(nums2):
            temp.append(element2)
        temp.sort()     ###这里携程temp = temp.sort()就会报错
        print(temp)
        if len(temp)%2 == 1:
            return temp[int((len(temp)-1)/2)]
        else:
            return (temp[int(len(temp)/2)] + temp[int(len(temp)/2) -1]) / 2
