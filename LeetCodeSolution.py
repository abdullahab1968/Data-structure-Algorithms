#Welcome to leetcode questions solution.

####1 subject:arrays
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
####2 subject:arrays
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

nums=[3,2,2,3]
j=removeElement(nums,3)
for i in range(j):
    print(nums[i])