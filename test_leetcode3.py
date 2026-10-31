s = "No lemon, no melon!"
left=0

g=s.replace(" ","")
g=g.lower()
right=len(g)-1
while left < right:
    if not g[left].isalnum():
        left+=1
    elif not g[right].isalnum():
        right-=1
    elif g[left]!=g[right]:
        print('its not palindrome')

        break
    elif g[left]==g[right]:
        left+=1
        right-=1
if left==right:
    print('its palindrome')

nums = [12, 7, 3, 9, 15, 20]
#reverse the array
#Time O(n), Space O(1)
left=0
right=len(nums)-1
while left<right:
    nums[left],nums[right]=nums[right],nums[left]
    left+=1
    right-=1
print(nums)

nums = [1, 2, 4, 6, 8, 11]
target = 10
left=0
right=len(nums)-1
while left<right:
    if nums[left]+nums[right]<target:
        left+=1
    elif nums[left]+nums[right]>target:
        right-=1
    elif nums[left]+nums[right]==target:
        print(left,right,'these are indices')
        break


nums = [1, 1, 2, 3, 3, 4, 5, 5, 6]
target = 7
#Time O(n), Space O(1) extra, excluding output
left=0
right=len(nums)-1
while left<right:
    if nums[left]+nums[right]>target:
        right-=1
    elif nums[right]+nums[left]<target:
        left+=1
    elif nums[right]+nums[left]==target:
        print(nums[left],nums[right])
        left+=1
        right-=1
        while left<right and left==left-1:
            left+=1
        while left<right and right==right-1:
            right-=1


nums = [2, 3, 5, 7, 9, 12]
target = 14
left=0
right=len(nums)-1
while left<right:
    if nums[left]+nums[right]<target:
        left+=1
    elif nums[left]+nums[right]>target:
        right-=1
    elif nums[left]+nums[right]==target:
        print(True)
        break
    else:
        print(False)
nums = [4, 6, 2, 8, 3]
#[0, 4, 10, 12, 20]
#Target: Time O(n), Space O(n)
left=0
b=[]
for x in range(len(nums)):
    b.append(left)
    left+=nums[x]

print(b)
nums = [4, 9, 4, 2, 9, 4, 7, 2, 9, 9]
#Return the number that appears most frequently.
dic={}

#Target: Time O(n) average, Space O(n)

for x in nums:
    if x in dic:
        dic[x]+=1
    else:
        dic[x]=1
b=sorted(dic,key=dic.get,reverse=True)
print(b[0])#when we do sorted then it makes list so we did index

nums = [8, 3, 11, 6, 4]
target = 14
dic={}
for index,number in enumerate(nums):

    if target-number not in dic:
        dic[number]=index
    else:
        print(dic[target-number],index)

#9. Nearby Duplicate
#Hash Map
nums = [7, 2, 9, 4, 7, 8]
k = 4
#Time O(n) average, Space O(n)
dic={}
#without hash
for x in range(len(nums)):
    if nums[x]<=nums[x+k]:
        print(True)
        break
    else:
        print(False)

#with hash
nums = [7, 2, 9, 4, 7, 8]
k = 4
#Time O(n) average, Space O(n)
dic={}
for index,number in enumerate(nums):
    if number not in dic:
        dic[number]=index
    elif number in dic:
        if dic[number]-index<=k:
            print(True)
         
print(dic)


#10. Maximum Sum of a Fixed-Size Window
#Fixed Sliding Window
nums = [3, 8, 2, 6, 5, 9, 1]
k = 3
#Time O(n), Space O(1)]

initial=nums[0]+nums[1]+nums[2]
current_sum=initial
max_sum=0
left=0
max_sum=max(max_sum,current_sum)
for x in nums[k:]:
    
    current_sum=initial+x-nums[left]
    max_sum=max(max_sum,current_sum)
    left+=1

print(max_sum)

#11. Minimum Sum of a Fixed-Size Window
#Fixed Sliding Window
nums = [7, 2, 5, 1, 6, 3, 4]
k = 4
#Time O(n), Space O(1)
initial=nums[0]+nums[1]+nums[2]+nums[3]
current_sum=initial
min_sum=0
left=0
min_sum=max(min_sum,current_sum)
for x in nums[k:]:
    
    current_sum=initial+x-nums[left]
    min_sum=min(max_sum,current_sum)
    left+=1

print(min_sum)
#12. Longest Subarray Without Duplicates

nums = [2, 5, 7, 5, 3, 1, 4, 3, 8]
#Find the length of the longest contiguous subarray that contains no duplicate values.

#Target: Time O(n) average, Space O(n)
max_len=0
b=set()
left=0
for x in nums:
   
    if x not in b:
        b.add(x)
        max_len=max(len(b),max_len)
    else:
        while x in b:
            b.remove(nums[left])
            left+=1
        b.add(x)
        max_len=max(len(b),max_len)
print(max_len)    


#13. Maximum Subarray Sum
#Kadane's Algorithm
nums = [-4, 6, -2, 3, -1, 5, -8, 4]

#Find the maximum sum of any non-empty contiguous subarray.

#Time O(n), Space O(1
current_sum=0
max_sum=0
for x in nums:
    current_sum+=x
    max_sum=max(max_sum,x,current_sum)
    current_sum=max(x,current_sum)

print(max_sum)

#14. Move Zeroes

nums = [0, 5, 0, 1, 0, 8, 3, 0]
#Time O(n), Space O(1)
left=0
for x in range(len(nums)):
    if nums[x] != 0:
        nums[x],nums[left]=nums[left],nums[x]
        left+=1
print(nums)

#15. Remove Duplicates from a Sorted Array
#Two Pointers
nums = [1, 1, 2, 2, 2, 4, 5, 5, 7, 8, 8]
     #   1,2,4,5
#Time O(n), Space O(1)
left=1
for x in range(len(nums)):
    if nums[x] != nums[left]:
        if nums[x]!=nums[left-1]:
            nums[left]=nums[x]
            left+=1
    
print(nums[:6])


#16. Longest Consecutive Sequence

nums = [15, 6, 20, 7, 9, 8, 10, 2]
#Time O(n) average, Space O(n)
#Find the length of the longest consecutive sequence. The numbers don't need to be adjacent in the input.

#Expected answer: 5, from the sequence 6, 7, 8, 9, 10
b=set(nums)
g=set()
max_len=0
for x in b:
 
    if x-1 not in b:
        g.add(x)
        max_len=max(len(g),max_len)
        if x+1 in g:
            while x+1 in g:
                g.add(x)
                max_len=max(len(g),max_len)
                x+=1
print(max_len)
















    

