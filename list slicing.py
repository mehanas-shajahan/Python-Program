#list slicing
nums=[10,20,30,40,50,60]

print(nums[1:4])
print(nums[:3])
print(nums[3:])
print(nums[::2])
print(nums[-3:])
print(nums[::-1])
print(nums[:])

nums_1=[10,30,40,10]
print(10 in nums_1)
print(nums_1.count(10))
print(nums_1.index(30))

nums_2=[32,78,12,0,-9]
nums_2.sort()
print(nums_2)
nums_2.sort(reverse=True)
print(nums_2)

nums_3=[4,3,2,1]
nums_3.reverse()
print(nums_3)

nums_4=[56,78,2,3,6,9,4,5,1,90,45,23,78,90,345,788,12]
print(len(nums_4))
print(sum(nums_4))
print(min(nums_4))
print(max(nums_4))
