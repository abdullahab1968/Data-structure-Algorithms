#Hashing functions 
#for strings 

def sascii(str,m):
    sum=0
    for ch in str:
        sum+=ord(ch)
    return sum%m        
#print(sascii("ABCDEFGH",16))


#Sorting methods

#1) Bubble Sort:

def bubble_sort(arr):
    n=len(arr)
    for i in range(0,n): 
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j] #Swap between them
# arr=[20,10,30,40,1,4,-1]
# bubble_sort(arr)
# print(arr)


#2) Selection Sort:

def selection_sort(arr):
    n=len(arr)
    for i in range(0,n):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        if min!=i:
            arr[i],arr[min]=arr[min],arr[i]        


# arr=[20,10,30,40,1,4,-1,100,9]
# print(arr)
# selection_sort(arr)
# print(arr)

#3) Insertion sort

def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        current_num=arr[i]
        j=i
        while j>0  and arr[j-1]>current_num  :
            arr[j]=arr[j-1]
            j-=1
        arr[j]=current_num       

# arr=[30,10,50,20,60,1]
# print(arr)
# insertion_sort(arr)
# print(arr)

#4) Bucket sort
import math
def bucket_sort(arr):
    # number of buckets we need.
    num_of_bucks=math.floor(math.sqrt(len(arr)))
    #creat list of lists 
    buckets=[[] for _ in range(num_of_bucks)]
    # Find the maximum value for the array
    max_arr=max(arr)
    # loop on each element and put into their pucket
    for i in range(0,len(arr)):
        #calculate the appropriate bucket for each element
        appropriate_bucket=math.ceil((arr[i] * num_of_bucks)/max(arr))
        #append each element to appropriate bucket
        buckets[appropriate_bucket-1].append(arr[i])
        
    #Sort each bucket individual
    for i in range(num_of_bucks):
        bubble_sort(buckets[i])
        
    arr.clear()
    for i in range(num_of_bucks):
        arr+=buckets[i]
        
    print(arr)

    

# buckets=[20,40,10,50,60,90,30,100,70]
# bucket_sort(buckets)
# print(buckets)    

#5) Merge sort

def merge_sort(arr):
      if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              arr[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                arr[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k]=right[j]
            j += 1
            k += 1


# arr=[20,10,30,15]   
# merge_sort(arr)
# print(arr)

#6) Quick sort:

