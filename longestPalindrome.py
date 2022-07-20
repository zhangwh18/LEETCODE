import numpy as np
from numpy import unravel_index


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return ''
        else:
            comm = np.zeros((len(s), len(s)))
            for i in range(len(s)):
                for j in range(i+1, len(s)):
                    if s[i] == s[j]:
                        comm[i][j] = j-i
                        break
                # continue
            result = unravel_index(np.argmax(comm), comm.shape)
            print(result[0], result[1])
            if result[0] or result[1]:
                lpa = []
                for i in range(result[0], result[1]):
                    lpa.append(s[i])
                lpa.append(s[i+1])
                str1 = ''.join(lpa)
                return str1
            else:
                return ''


num = Solution()
s = "abckhskhflhasifh"
print(type(len(s)))
print(num.longestPalindrome("aacabdkacaa"))
