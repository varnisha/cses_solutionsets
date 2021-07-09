n=int(input())
nums=list(map(int,input().split()))
#Formula for sum of natural numbers = (n*(n+1))/2
missing_number=((n*(n+1))/2)-sum(nums)
print(int(missing_number))
