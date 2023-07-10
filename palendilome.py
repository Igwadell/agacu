def solution(inputString):
    for a in range(len(inputString)):
        if inputString[a] == inputString[-(a+ 1)]:
            continue
        else: 
            return False
    return True
