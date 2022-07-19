class Solution(object):
    def __init__(self, s):
        self.s = s

    def romanToInt(abc):
        # print(len(abc.s))
        """
        :type s: str
        :rtype: int
        """
        num = 0
        c = 0
        while c < len(abc.s):
            print(abc.s[c])
            print(c)
            # c = c+1
            switcher = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000,
            }
            if c < len(abc.s)-1:
                if switcher.get(abc.s[c]) < switcher.get(abc.s[c+1]):
                    num = num+switcher.get(abc.s[c+1])-switcher.get(abc.s[c])
                    c = c+2
                else:
                    num = num+switcher.get(abc.s[c])
                    c = c+1
            else:
                num = num+switcher.get(abc.s[c])
                c = c+1
                #     if c == len(abc.s)-1:
                #         num = switcher.get(abc.s[c])+num
                #     else:
                #         if num > switcher.get(abc.s[c-1]):
                #             num = num+num-switcher.get(abc.s[c-1])
                #         else:
                #             num = num+switcher.get(abc.s[c-1])
                # # print(len(abc.s))
            print(num)


num = Solution("III")

num.romanToInt()
# print("Hello")
# print(type(num))
# print(num.s)
