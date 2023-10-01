def calculateSum(members: list):
    if members.__len__() == 0:
        return 0
    else:
        value = 0
        for i in members:
            value += i
        return value

def calculateProduct(members: list):
    if members.__len__() == 0:
        return 1
    else:
        out = 1
        for i in members:
            out *= i
        return out

if __name__ == '__main__':
    assert calculateSum([]) == 0
    assert calculateSum([2,4,6,8,10]) == 30
    assert calculateProduct([]) == 1
    assert calculateProduct([1,2,3]) == 6