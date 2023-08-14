n = int(input())
 
nums = list(map(int, input().split()))
 
allOdd = allEven = True
for num in nums:
    if num%2:
        allEven = False
 
    else:
        allOdd = False
 
if allOdd or allEven:
    print(*nums)
 
else:
    print(*sorted(nums))
