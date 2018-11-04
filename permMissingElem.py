def solution(A):
    # write your code in Python 3.6
    A.sort()
    length = len(A)
    if(length == 0): return 1
    return sum(range(1, length+2)) - sum(A)

print(solution([1,2,3,5])) 