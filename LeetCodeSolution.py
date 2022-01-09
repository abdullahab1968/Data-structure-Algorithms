#Welcome to leetcode questions solution.

####1 subject:arrays Easy
# Given an integer array nums sorted in non-decreasing order,
#  remove the duplicates in-place such that each unique element appears only once.
#  The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages,
#  you must instead have the result be placed in the first part of the array nums.
#  More formally, if there are k elements after removing the duplicates, 
# then the first k elements of nums should hold the final result.
#  It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array. 
# You must do this by modifying the input array in-place with O(1) extra memory.

def removeDuplicates(self, nums) -> int:
    if not nums:
       return 0
      #save the location of the first duplicate to swap it with differnt value
    i=fir_dup=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[fir_dup]=nums[i]
            fir_dup+=1
    return fir_dup
####2 subject:arrays Easy
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

# Since it is impossible to change the length of the array in some languages
# , you must instead have the result be placed in the first part of the array nums.
#  More formally, if there are k elements after removing the duplicates,
#  then the first k elements of nums should hold the final result. 
# It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. 
# You must do this by modifying the input array in-place with O(1) extra memory.                
def removeElement( nums, val):
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]==val:
                nums[i]=nums[j]
                nums[j]='_'
                j-=1
            if nums[i]!=val:
                i+=1
        return j+1       

# nums=[3,2,2,3]
# j=removeElement(nums,3)
# for i in range(j):
#     print(nums[i])

####3) subject arrays Easy
# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.


def isPalindrome(x):
    str_num=str(x)
    i=0
    j=len(str_num)-1
    
    while i<j:
        if str_num[i]!=str_num[j]:
            return False
        i+=1
        j-=1
    return True        
# print(isPalindrome(411124))

####4) Strings Easy
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

def longestCommonPrefix(strs):
    if len(strs)==1:
        return strs[0]
    longest_prefix=0
    i=0
    for i in range(len(strs)-1):
            j=0
            while j<len(strs[i]) and j<len(strs[i+1]):
                if strs[i][j]==strs[i+1][j]:
                   j+=1
                   
                else: 
                    break
            if i==0:
                longest_prefix=j    
            elif j<longest_prefix:        
               longest_prefix=j
            if longest_prefix==0:
                return ""
               
            
    return strs[0][:longest_prefix]
    
# print("hello:",longestCommonPrefix(["flower","flow","floigt"]))

####5) Array Easy
# Given an array of integers nums and an integer target,
#  return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
#  and you may not use the same element twice.

# You can return the answer in any order.

def twoSum( nums, target):
        dict={}
        for i in range(len(nums)):
            dict[nums[i]]=i
        
        for  i in range(len(nums)):
            sec_value=target-nums[i]
            if sec_value in dict and dict[sec_value]!=i:
                return [i,dict[sec_value]]
            
# print(twoSum([2,1,3],4))            

####6) strings Medium:
#Given a string s, 
# find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring( s):
       
          dic, res, start, = {}, 0, 0
          for i, ch in enumerate(s):
            if ch in dic:
               res = max(res, i-start) # update the res
               start = max(start, dic[ch]+1)  # here should be careful, like "abba"
            dic[ch] = i
          return max(res, len(s)-start) 

# print("result: ",lengthOfLongestSubstring("bbtablud"))