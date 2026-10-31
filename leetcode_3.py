s = "No lemon, no melon!"
#Target: Time O(n), Space O(1)

b=s.replace(" ","")
b=b.lower()
left=0
right=len(b)-1
print(b)
while left<right:
    if b[left].isalnum:
        left+=1
    elif b[right].isalnum:
        right-=1
    elif b[left]==b[right]:
        left+=1
        right-=1
    elif b[left]!=b[right]:
        print('its not palindrome')
        print(b[left],b[right])
        break

print('its palidrome')


nums = [12, 7, 3, 9, 15, 20]

#Target: Time O(n), Space O(1)
left=0
right=len(nums)-1
while left<right:
    nums[left],nums[right]=nums[right],nums[left]
    left+=1
    right-=1

print(nums)

nums = [1, 2, 4, 6, 8, 11]
target = 10
#Find a pair whose sum equals 10. Return the pair of values.
#Target: Time O(n), Space O(1)
left=0
right=len(nums)-1
while left<right:
     if nums[left]+nums[right]>target:
         right-=1
     elif nums[left]+nums[right]<target:
         left+=1
     elif nums[left]+nums[right]==target:
         print(nums[left],nums[right])
         break
     

nums = [1, 1, 2, 3, 3, 4, 5, 5, 6]
target = 7
#Find every unique value pair whose sum equals 7. Do not print duplicate pairs.
#Target: Time O(n), O(1) extra space excluding output
left=0
right=len(nums)-1
temp=[]
while left<right:
    if nums[left]==nums[left+1]:
        left+=1
    elif nums[right]==nums[right-1]:
        right-=1
    elif nums[right]+nums[left]==target:
        print(nums[left],nums[right])
        left+=1
        right-=1
    
nums = [2, 3, 5, 7, 9, 12]
target = 14

#Return True if two different elements sum to 14; otherwise, return False.
#Expected: True
#Target: Time O(n), Space O(1)

left=0
right=len(nums)-1
while left<right:
     if nums[left]+nums[right]>target:
         right-=1
     elif nums[left]+nums[right]<target:
         left+=1
     elif nums[left]+nums[right]==target:
         print(True)
         break
     elif left>right:
         print(False)


#6. Prefix Sum
nums = [4, 6, 2, 8, 3]
#Create a prefix-sum array using the approach we practiced: append the running total before adding the current number.
#[0, 4, 10, 12, 20]
left=0
b=[]
#Target: Time O(n), Space O(n)
for x in nums:
    b.append(left)
    left+=x
print(b)

nums = [4, 9, 4, 2, 9, 4, 7, 2, 9, 9]
#Return the number that appears most frequently.
#Expected: 9
#Target: Time O(n) average, Space O(n)
dic={}
for x in nums:
    if x in dic:
        dic[x]+=1
    elif x not in dic:
        dic[x]=1
b=sorted(dic,key=dic.get,reverse=True)
print(b[0])

#8. Two Sum — Unsorted Array
nums = [8, 3, 11, 6, 4]
target = 14



#Return the indices of one pair whose sum equals 14. Do not sort the array.
#One valid answer: [1, 2], because nums[1] + nums[2] = 3 + 11 = 14.
#Target: Time O(n) average, Space O(n)
dic={}
for index,number in enumerate(nums):
    if target-nums[index] in dic:
        print(index,dic[target-nums[index]],'here')
        break
    else:
        dic[number]=index

nums = [7, 2, 9, 4, 7, 8]
k = 4
#Return True if the same value occurs at two different indices whose distance is at most k.
#Expected output: True
#Target: Time O(n) average, Space O(n)
dic={}
left=0
for index,number in enumerate(nums):
    if number not in dic:
        dic[number]=index
    elif number in dic:
        if dic[number]-index <= k:
            print(True)
            print(dic[number],number)
            break
        else:
            print(False)
nums = [3, 8, 2, 6, 5, 9, 1]
k = 3
#Find the maximum sum of any contiguous subarray of length 3.
#Expected output: 20
#Target: Time O(n), Space O(1)
left=0
sum_count=nums[0]+nums[1]+nums[2]
max_count=sum_count
for x in nums[3:]:
    sum_count+=x
    sum_count-=nums[left]
    max_count=max(max_count,sum_count)
    left+=1

print(max_count)

nums = [7, 2, 5, 1, 6, 3, 4]
#Find the minimum sum of any contiguous subarray of length 4.
#Expected output: 14
#Target: Time O(n), Space O(1)
left=0
sum_count=nums[0]+nums[1]+nums[2]+nums[3]
min_count=sum_count
for x in nums[4:]:
    sum_count+=x
    sum_count-=nums[left]
    min_count=min(min_count,sum_count)
    left+=1

print(min_count)

nums = [2, 5, 7, 5, 3, 1, 4, 3, 8]
#Find the length of the longest contiguous subarray containing no duplicate values.
#Expected output: 5
#Target: Time O(n) average, Space O(n
sub_arr=set()
left=0
max_len=0
for x in range(len(nums)):
    if nums[x] not in sub_arr:
        sub_arr.add(nums[x])
        max_len=max(len(sub_arr),max_len)
        

    elif nums[x] in sub_arr:
        while nums[x] in sub_arr:
            sub_arr.remove(nums[left])
            left+=1
        sub_arr.add(nums[x])
        max_len=max(len(sub_arr),max_len)
print(max_len)

nums = [-4, 6, -2, 3, -1, 5, -8, 4]
#Find the maximum sum of any non-empty contiguous subarray.
#Expected output: 11
#Target: Time O(n), Space O(1)
sub_mum=nums[0]
left=0
total_sum=0
for x in nums[1:]:
    sub_mum+=x
    total_sum=max(total_sum,sub_mum)
    sub_mum=max(sub_mum,x)

print(total_sum)

nums = [0, 5, 0, 1, 0, 8, 3, 0]
#Move all zeroes to the end, preserving the order of 
# non-zero numbers. Modify the original array without creating another array.
#Expected output:
#[5, 1, 8, 3, 0, 0, 0, 0]
#Target: Time O(n), Space O(1)
left=0
for x in range(len(nums)):
    if nums[x] != 0:
        nums[left],nums[x]=nums[x],nums[left]
        left+=1

print(nums)    

nums = [1, 1, 2, 2, 2, 4, 5, 5, 7, 8, 8]
#Remove duplicates in-place, keeping only one copy of each value.
#  Print the useful portion of the array.
#Expected useful portion:
#[1, 2, 4, 5, 7, 8]
#Target: Time O(n), Space O(1)
left=1
g=0
for x in range(len(nums)):
     if g!=nums[x]:
        if nums[left] != nums[x]:
           
           nums[left]=nums[x]
           left+=1
        g=nums[x]
print(nums)


        










        
