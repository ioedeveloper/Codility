def solution(N):
    # write your code in Python 3.6
    if(N < 1):
        return 0
    else:
        binaryEquivalent = "{0:b}".format(N)
        strBinary = str(binaryEquivalent)
        
        savedGap = []
        countGap = 0
        start = 0
        for i in strBinary:
            if(start == 0):
                start = int(i)
            elif(start == 1 and int(i) == 0):
                countGap += 1
            elif(start == 1 and int(i) == 1):
                start = 1
                savedGap.append(countGap)
                countGap = 0
        if(savedGap==[]):
            binaryGap = 0
        else:
            binaryGap = max(savedGap)
        return binaryGap

print(solution(328))