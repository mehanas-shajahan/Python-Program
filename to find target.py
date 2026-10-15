#two sum
nums=[]
n=int(input())
for i in range(n):
    data=int(input())
    nums.append(data)
target=int(input())
found=False
for i in range(n):
    for j in range(i+1,n):
        if nums[i]+nums[j]==target:
            print(f"{i} , {j}")
            found=True
            break
    if found:
        break
if not found:
    print(-1,-1)