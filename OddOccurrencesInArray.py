def solution(A):
    # write your code in Python 3.6
    visited = []
    for i in range(len(A)):
        if i not in visited:
            if((i+2) < len(A)):
                if(A[i+2] != A[i]):
                    return A[i]
                visited.append(A[i])
                visited.append(A[i+2])
            else:
                return A[i]