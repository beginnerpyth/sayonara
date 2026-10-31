s = "No lemon, no melon!"
no_space=s.replace(" ","")
s=no_space.lower()
print(s)
right=len(s)-1
left=0
while left<right:
    if not s[right].isalpha():
        right-=1
    elif not s[left].isalpha():
        left+=1
    elif s[left]!=s[right]:
        print('its not palindrome')
        print(s[left])
        print(s[right])
        break
    elif s[left]==s[right]:
        left+=1
        right-=1
    elif left>right:
        print('its palindrome')
        break


nums = [12, 7, 3, 9, 15, 20]
right=len(nums)-1
left=0
while left < right:
    nums[left],nums[right]=nums[right],nums[left]
    left+=1
    right-=1
print(nums)

nums = [1, 2, 4, 6, 8, 11]
target = 10

left=0
right=len(nums)-1
while left<right:
    if nums[left]+nums[right]>target:
        right-=1
    elif nums[left]+nums[right]<target:
        left+=1
    else:
        print(nums[left],nums[right])
        break

nums = [1, 1, 2, 3, 3, 4, 5, 5, 6]
target = 7
left=0
right=len(nums)-1
dic={}
while left<right:
    
    if nums[left]+nums[right]>target:
        right-=1
    elif nums[left]+nums[right]<target:
        left+=1
    else:
        baba=[nums[left],nums[right]]
        print(baba)
        left+=1
        right-=1
        while left < right and left==left-1:
            left+=1
        while left < right and right==right-1:
            right -=1
        

nums = [2, 3, 5, 7, 9, 12]
target = 14
left=0
right=len(nums)-1
while left<right:
    if nums[left]+nums[right]<target:
        left+=1
    elif nums[left]+nums[right]>target:
        right-=1
    else:
        if nums[left]+nums[right]==target:
            print(True)
            break
        else:
            print(False)
            break

nums = [4, 6, 2, 8, 3]
left=0
b=[]

for x in nums:
    
    b.append(left)
    left=left+x

print(b)

nums = [4, 9, 4, 2, 9, 4, 7, 2, 9, 9]
dic={}
for x in nums:
    if x  in dic:
        dic[x]+=1
    else:
        dic[x]=1

print(max(dic,key=dic.get))

nums = [8, 3, 11, 6, 4]
target = 14
left=0
right=len(nums)-1
dic={}
for index,number in enumerate(nums):
    if target-number not in dic:
        dic[number]=index
    else:
        print(dic[target-number],index)
    
    
nums = [7, 2, 9, 4, 1, 2]
k = 4
for x in range(len(nums)):
    if nums[x] == nums[x+k]:
        print(True)
        break
    elif x+k>len(nums):
        print(False,'there is not same number')
        break

#hashmap
nums = [7, 2, 9, 4, 7, 8]
k = 4
dic={}
for index,number in enumerate(nums):
    if number in dic:
        if index-dic[number]==4:
            print(True)
            break
    else:
        dic[number]=index
nums = [3, 8, 2, 6, 5, 9, 1]
k = 3
initial=nums[0]+nums[1]+nums[2]
max_val=0

right=k
left=0
for x in nums[k:]:
    
    max_val=max(max_val,initial)
    
    
    initial=initial+nums[right]-nums[left]
    right+=1
    left+=1
    


print(max_val)

nums = [7, 2, 5, 1, 6, 3, 4]
k = 4

initial=nums[0]+nums[1]+nums[2]+nums[3]
min_val=initial

right=k
left=0
for x in nums[k:]:
    
    min_val=min(min_val,initial)
    
    
    initial=initial+nums[right]-nums[left]
    right+=1
    left+=1

print(min_val)

nums =  [1, 2, 3, 4, 1, 2, 5, 4]
#find the length of longest contigous subarray
b=set()
max_len=0
left=0

for x in range(len(nums)):
    if nums[x] not in b:
        b.add(nums[x])
        max_len=max(max_len,len(b))

    elif nums[x] in b:
        while nums[x] in b:#5,again it sees 5,it sees 3,again sees 3,again sees 3
            b.remove(nums[left])#first it deletes the 2,it deltes 5,it removes 7,removes 5,removes 3
            left+=1#left becomes 1,left becomes 2,3,,4,5
        b.add(nums[x])
        max_len=max(max_len,len(b))



print(max_len)


nums = [-4, 6, -2, 3, -1, 5, -8, 4]
#Find the maximum sum of a contiguous subarray.
max_sum=0
current_sum=0
for x in nums:
     current_sum+=x
     max_sum=max(current_sum,x,max_sum)
     current_sum=max(current_sum,x)
   



print(max_sum)


nums = [2, 5, 7, 5, 3, 1, 4, 3, 8]
b=set()
max_len=0
left=0
for x in nums:
    if x not in b:
        b.add(x)
        max_len=max(max_len,len(b))
    elif x in b:
        while x in b:
            b.remove(nums[left])
            left+=1
          
        b.add(x)
        max_len=max(max_len,len(b))

print(max_len)


nums = [0, 5, 0, 1, 0, 8, 3, 0]
#Move all zeroes to the end in-place, preserving the order of non-zero values.
same_value=nums[0]
left=0
for x in range(len(nums)):
    if nums[x] != same_value:
        nums[x],nums[left]=nums[left],nums[x]
        left+=1

print(nums)        

nums = [1, 1, 2, 2, 2, 4, 5, 5, 7, 8, 8]
        #1,2,4,5

#Remove duplicates in-place, leaving one copy of each value.

#Expected useful portion:

#Time: O(n)
#Space: O(1)
c=set()
left=1
g=0
for x in range(len(nums)):
    if g!=nums[x]:
        if nums[left] != nums[x]:
            nums[left]=nums[x]
            g=nums[left]
            left+=1


print(nums)

nums = [15, 6, 20, 7, 9, 8, 10, 2]
#Time: O(n) average
#Space: O(n)

ad=set(nums)
s=[]
max_len=0
for x in ad:
    if x-1 not in ad:
        s=[]
        s.append(x)
        max_len=max(max_len,len(s))
        b=x+1
        while b in ad:

            s.append(b)
            max_len=max(max_len,len(s))
            b+=1
    elif x+1 not in ad:
        s=[]
        s.append(x)
        max_len=max(max_len,len(s))
            
print(max_len)













































