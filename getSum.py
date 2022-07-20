class Solution(object):
    def getSum(self, a, b):
        array = []
        if a >= 0 and b >= 0:
            for i in range(a):
                # print(i)
                array.append(1)
            for i in range(b):
                # print(i)
                array.append(1)
            if len(array) is None:
                return 0
            else:
                return len(array)
        if a <= 0 and b <= 0:
            for i in range(abs(a)):
                # print(i)
                array.append(1)
            for i in range(abs(b)):
                # print(i)
                array.append(1)
            if len(array) is None:
                return 0
            else:
                return -len(array)
        if a <= 0 and b >= 0:
            # print(1)
            if abs(a) >= abs(b):

                for i in range(abs(a)):
                    # print(i)
                    array.append(1)
                for i in range(abs(b)):

                    del array[0]
                if len(array) is None:
                    return 0
                else:
                    return -len(array)
            else:

                for i in range(abs(b)):
                    # print(i)
                    array.append(1)
                for i in range(abs(a)):
                    # print(i)
                    del array[0]
                if len(array) is None:
                    return 0
                else:
                    return len(array)
        if a >= 0 and b <= 0:
            if abs(a) >= abs(b):

                for i in range(abs(a)):
                    # print(i)
                    array.append(1)
                for i in range(abs(b)):
                    # print(i)
                    del array[0]
                if len(array) is None:
                    return 0
                else:
                    return len(array)
            else:

                for i in range(abs(b)):
                    # print(i)
                    array.append(1)
                for i in range(abs(a)):
                    # print(i)
                    del array[0]
                if len(array) is None:
                    return 0
                else:
                    return -len(array)


num = Solution()
# for i in range(0):
#     print(i)
print(num.getSum(-1, 1))
# if -2 < 0:
#     print(1)
print(222 & 101)
