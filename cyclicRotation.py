def solution(A, K):
    # write your code in Python 3.6
    maxIndex = len(A)-1
    if (len(A) < 2):
        return A
    else:
        for i in range(K):
            for index in range(len(A)):
                if(index == maxIndex):
                    A[0] = replacedValue
                else:
                    if(index > 0):
                        replacedWith = replacedValue
                        replacedValue = A[index+1]
                        A[index+1] = replacedWith
                    else:
                        replacedValue = A[index+1]
                        replacedWith = A[index]
                        A[index+1] = replacedWith
        return A

print(solution([5, -1000], 1))