#convert roman into integer number.
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1,"V":5,"X":10,"L":50,"IX":9,"C":100,"D":500,"M":1000}
        res =0
        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i]]<roman[s[i+1]]:
                res = res-roman[s[i]]
            else:
                res = res+roman[s[i]]

        return res
s=Solution()
print(s.romanToInt("III"))#3

