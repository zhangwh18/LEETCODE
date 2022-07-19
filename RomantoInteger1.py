class Solution:
    def romanToInt(self, s):
        rDict = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
        z = 0
        p = -1
        for x in range(len(s)):

            if p == -1:
                z = z + rDict[s[x]]
                # print(z)
            elif rDict[s[p]] >= rDict[s[x]]:
                z = z + rDict[s[x]]
            else:
                z = z + rDict[s[x]]-2*rDict[s[p]]
            p = x
        return z


num = Solution()

print(num.romanToInt("IV"))
# print("Hello")
# print(type(num))
# print(num.s)
