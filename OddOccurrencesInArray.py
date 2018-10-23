def solution(A):
    # write your code in Python 3.6
    A.sort()
    if(len(A) == 1):
        return A[0]
    for i in range(0, len(A), 2): 
        if((i+1) < len(A)):
            if(A[i+1] != A[i]):
                return A[i]
        else:
            return A[i]

print(solution([9, 3, 9, 3, 9, 7, 9]))