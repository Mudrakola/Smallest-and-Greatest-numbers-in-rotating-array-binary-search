def get_small_large( A):
    left = 0
    right = len(A)-1
    while left < right:
        mid = (left+right)//2
        if A[left] < A[right] or A[mid] < A[left]:
            right = mid
        else:
            left = mid+1
    print(left)
    return left
num=int(input())
A=list(map(int,input().split()))
result=get_small_large(A)
print(str(A[result])+" "+str(A[result-1]))