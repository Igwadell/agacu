def solution(inputArray):
    emptylist = []
    for a in range(len(inputArray)-1):
        b = inputArray[a] * inputArray[a +1]
        emptylist.append(b)
    great = max(emptylist)
    return great
