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

def average(members: list):
    if members.__len__() == 0:
        return 0
    else:
        total = 0
        for i in members:
            total += i
        return total / members.__len__()

def median(members: list):
    length = members.__len__()
    if length == 0:
        return 0
    else:
        members = sorted(members)
        if length % 2 == 0:
            positions = [int(length/2), int((length/2) - 1)]
            median = (members[positions[0]] + members[positions[1]]) / 2
        else:
            position = int((length - 1) / 2)
            median = members[position]

        return median


if __name__ == '__main__':
    assert calculateSum([]) == 0
    assert calculateSum([2,4,6,8,10]) == 30

    assert calculateProduct([]) == 1
    assert calculateProduct([1,2,3]) == 6

    assert median([1,3,2,8]) == 2.5
    assert median([1,2,3,9,8]) == 3

    print('all passed')

    print('sum of [] =', calculateSum([]))
    print('sum of [2,4,5,8,10] =', calculateSum([2,4,6,8,10]))

    print('product of [] =', calculateProduct([]))
    print('product of [1,2,3] =', calculateProduct([1,2,3]))

    print('average of [] =', average([]))
    print('average of [1,2,3,4,5] =', average([1,2,3,4,5]))

    print('median of [1,3,2,8] =', median([1,3,2,8]))
    print('median of [1,2,3,9,8] =', median([1,2,3,9,8]))


