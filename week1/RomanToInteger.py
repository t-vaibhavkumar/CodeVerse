class Solution:
    def romanToInt(self, s: str) -> int:
        l = {'I': 1, 'V': 5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
        prev = 0
        num = 0
        for i in reversed(s):
            if(l[i]<prev):
                num = num-l[i]
            else:
                num = num + l[i]
                prev = l[i]
        return num