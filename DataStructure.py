##Create nodes
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList():
    def __init__(self):
        self.head=None

    def insert_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_last(self,data):
        new_node=Node(data)
        iter=self.head
        if iter==None:
            new_node.next=None
            self.head=new_node
        else:
            while iter.next!=None:
                iter=iter.next
            iter.next=new_node
            new_node.next=None     
    def traversal(self):
        iter=self.head
        if iter==None:
            print("Linked List is empty")
        while iter:
            print(iter.data)
            iter=iter.next
        
    def delete_node(self,data):
        current=self.head
        #if the linked list is empty
        if current==None:
            print('Linked List is empty')
           
        #if the remove elemnt in the begining of the linked list
        else:
            if self.head.data==data:
                self.head=self.head.next
                current.next=None
            else:
                while current :
                    prev=current
                    current=current.next
                    if current and current.data==data:
                        prev.next=current.next
                    
               

        #if the elemnt in the linked list.
#####Stack:
# LIFO Method
from audioop import reverse
from collections import deque
from distutils import dist
from inspect import stack
import queue
from random import random
from time import time
from unittest import result
from xml.etree.ElementTree import C14NWriterTarget
my_stack=deque()
my_stack.append(1)
my_stack.append(2)
my_stack.pop()
#Queue
q=deque()
q.append(1)
q.append(2)
q.append(3)
q.popleft()
q.popleft()
q.popleft()


#Graphs:
# from collections import defaultdict
# class Graph:
#     def __init__(self,vertices):
        

#BFS Alforithm

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : ['A'],
  'E' : ['F'],
  'F' : []
}

def bfs(graph,node):
    queue=deque()
    visited=[]
    queue.append(node)
    while len(queue)!=0:
        p=queue.popleft()
        if p not in visited:
            print(p)
            visited.append(p)
            for neighbor in graph[p]:
                if neighbor not in visited:
                    queue.append(neighbor)
      




#DFS algorithm:
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : ['A'],
  'E' : ['F'],
  'F' : []
}
def dfs(graph,node):
    s=deque()
    visited=[]
    s.append(node)
    while s:
        p=s.pop()
        if p not in visited:
           print(p)
           visited.append(p)
           for neighbor in graph[p]:
               if neighbor not in visited:
                  s.append(neighbor)

#### Topological sort Algorithm
def topo_logical_sort(graph):
    visited=[]
    stack=deque()
    for v in graph:
        if v not in visited:
            topo_sort(graph,v,visited,stack)
    while stack:
        print(stack.pop())

def topo_sort(graph,v,visited,stack):
    for edge in graph[v]:
        if edge not in visited:
            topo_sort(graph,edge,visited,stack)
    stack.append(v)
    visited.append(v)        

graph = {
  'A' : ['C'],
  'B' : ['C','E'],
  'C' : ['D'],
  'D' : ['F','H'],
  'E' : [],
  'F' : ['G'],
  'G' : [],
  'H' :[]
}
# topo_logical_sort(graph)

#### SSSP(Singe Source Shortest Path)
def bfs_sssp(graph,source):
    queue=deque()
    parents={}
    visited=set()
    queue.append(source)
    parents[source]=None
    while queue:
        current_vertex=queue.popleft()
        for adj in graph[current_vertex]:
            if adj not in visited:
                queue.append(adj)
                if adj not in parents:
                    parents[adj]=current_vertex
        visited.add(current_vertex)            
    print(parents)


graph={
1:[9,3,7],    
2:[8,1,4],
3:[1,4,5],
4:[3,2],
5:[3,6],
6:[5,7],
7:[1,6],
8:[9,0],
9:[1,8],
0:[8]
}
# bfs_sssp(graph,2)

####Dijkstra
from queue import PriorityQueue
def dijkstra(graph):
    pass
#parents
# #minheap to save the minimum
#     min_heap=[]
#     heapify(min_heap)

#     while min_heap:
#        curr=heappop(min_heap)
#        for adj in graph[curr]:
#            new_distance=distance[curr]+edge_distance
#            if  new_distance< distance[adj]:
#                distance[adj]=new_distance
#                parents[adj]=curr

####Greedy algorithm

####Activity Selection Problem
class Activity():
    def __init__(self,name,start_time,finish_time):
        self.name=name
        self.start_time=start_time
        self.finish_time=finish_time

    def to_string(self):
        print('name '+self.name+' start time: '+str(self.start_time)+' finish time: '+str(self.finish_time))

        

def activity_selection_problem(activities):
    activities.sort(key=lambda x:x.finish_time)
    previous_activity=activities[0]
    previous_activity.to_string()
    for i in range(1,len(activities)):
        if activities[i].start_time >= previous_activity.finish_time:
            previous_activity=activities[i]
            previous_activity.to_string()

# A1=Activity('A1',0,6)
# A2=Activity('A2',3,4)
# A3=Activity('A3',1,2)
# A4=Activity('A4',5,8)
# A5=Activity('A5',5,7)
# A6=Activity('A6',8,9)
# act=[A1,A2,A3,A4,A5,A6]
# activity_selection_problem(act)

####Coin Change problem:
def coin_change_problem(value,coins):
    result=0
    my_str='Break down:'
    i=len(coins)-1
    while value>0:
        if value>=coins[i]:
            value-=coins[i]
            result+=1  
       
        else:
            if result!=0:
               my_str+=' Rs. '+str(coins[i])+'*'+str(result)
               result=0
            i-=1 
    if result!=0:
               my_str+=' Re. '+str(coins[i])+'*'+str(result)    
    print(my_str)
# a=[1,2,5,10,20,50,100,500,1000]
# coin_change_problem(128,a)   

####Fractional Knapsack problem:
class Item:
    def __init__(self,name,value,weight):
        self.name=name
        self.value=value
        self.weight=weight
        self.ratio=value/weight
def fractional_knapsack(items,capacity):
    items.sort(key=lambda x:x.ratio,reverse=True) 
    result=0
    for item in items:
        if item.weight<=capacity:
            result+=item.value
            capacity-=item.weight
        else:
            result+=(capacity/item.weight) * item.value 
            capacity=0
    return result        
# items_name=['item1','item2','item3','item4','item5','item6']
# items_weight=[6,10,3,5,1,3]
# items_value=[6,2,1,8,3,5]
# items=[]
# for i in range(0,len(items_name)):
#     items.append(Item(items_name[i],items_value[i],items_weight[i]))

# print(fractional_knapsack(items,10))

####Divide and Conquer:
#Binary search:

def binary_search(arr,find_num,start,end):
   
    if end>=start:
        mid=(start+end) // 2
        if find_num == arr[mid]:
            return mid
        elif find_num < arr[mid]:
            return binary_search(arr,find_num,start,mid-1)
        elif find_num > arr[mid]:
            return binary_search(arr,find_num,mid+1,end)
       

    else: 
        return -1    

# arr=[10,20,30,40,50,60,70,80,90,100,110]
# print(binary_search(arr,50,0,len(arr)-1))

##Metge Sort:
def merge_sort(arr,left,right):
    if left<right:
        middle=(left+right)//2
        merge_sort(arr,left,middle)
        merge_sort(arr,middle+1,right)
        merge(arr,left,middle,right)
     

def merge(arr,left,middle,right):
    left_arr=arr[left:middle+1]
    right_arr=arr[middle+1:right+1]
    i=0
    j=0
    k=left
    while i<len(left_arr) and j<len(right_arr):
          if left_arr[i]<=right_arr[j]:
              arr[k]=left_arr[i]
              i+=1
          else:
              arr[k]=right_arr[j]
              j+=1
          k+=1
    while i<len(left_arr):
        arr[k]=left_arr[i]
        i+=1
        k+=1
    while j<len(right_arr):
        arr[k]=right_arr[j]
        j+=1
        k+=1
arr=[5,4,10,21]
merge_sort(arr,0,len(arr)-1)
#print(arr)            
#Dynamic programmming top down
def fibonacci_series(num,arr):
  if arr[num]<0:
      if num == 0:
          arr[num] = 0
      if num == 1:
        arr[num] = 1    
      elif arr[num] == -1:
        arr[num] = fibonacci_series(num-1,arr)+fibonacci_series(num-2,arr)
  return arr[num]
        # return fibonacci_series(num-1)+fibonacci_series(num-2)[Before dynamic programming]
num=8
arr=[-1]*(num+1)


# print(fibonacci_series(8,arr))
#### number factor

def ways_to_get(num):
    if num==0 or num==1 or num==2:
        return 1
    if num==3:
        return 2
    return ways_to_get(num-1)+ways_to_get(num-3)+ways_to_get(num-4)        
# print(ways_to_get(4))

#house theif:
def max_money_recursive(house_net_worth,curr_index):
    if curr_index>=len(house_net_worth):
        return 0
    steal_current_house=house_net_worth[curr_index]+max_money_recursive(house_net_worth,curr_index+2)
    skip_current_house=max_money_recursive(house_net_worth,curr_index+1)
    return max(steal_current_house,skip_current_house)    

# arr=[6,7,1,30,8,2,4]
# print(max_money_recursive(arr,0))

#Convert one string to another:
def conv_str1_str2(s1,s2,first_index,second_index):
    if first_index==len(s1):
        return len(s2)-second_index

    if second_index==len(s2):
        return len(s1)-first_index    

    if s1[first_index]==s2[second_index]:
        return conv_str1_str2(s1,s2,first_index+1,second_index+1)
    #delete operation
    c1=1+conv_str1_str2(s1,s2,first_index,second_index+1)
    #insert operation
    c2=1+conv_str1_str2(s1,s2,first_index+1,second_index)
    #replace operation
    c3=1+conv_str1_str2(s1,s2,first_index+1,second_index+1)
    return min(c1,c2,c3)
# print(conv_str1_str2('table','tgabe',0,0))    

#0/1 Knapsack problem:

def zero_one_knapsack(profits,weights,capacity,index):
    if index>=len(profits) or capacity<=0 or index<0 :
        return 0    
    s1=0
    if weights[index]<=capacity:
       s1=profits[index]+zero_one_knapsack(profits,weights,capacity-weights[index],index+1)
    s2=zero_one_knapsack(profits,weights,capacity,index+1)
    return max(s1,s2)
#example:
# profits=[31,26,73,17]
# weights=[3,1,5,2]
# print(zero_one_knapsack(profits,weights,7,0)  )  

#Longest common subsequence:
def longest_common_subsequence(s1,s2,i1,i2):
    if i1>=len(s1) or i2>=len(s2):
        return 0
    longest_sub1=0
    #case1 if the characters are equal
    if s1[i1]==s2[i2]:
       longest_sub1=1+longest_common_subsequence(s1,s2,i1+1,i2+1)
    #case2 if we increase the index of s2
    longest_sub2=longest_common_subsequence(s1,s2,i1,i2+1)
    #case3 if we increase the index of s1
    longest_sub3=longest_common_subsequence(s1,s2,i1+1,i2)   
    return max(longest_sub1,longest_sub2,longest_sub3)


# print(longest_common_subsequence('elephant','eretpat',0,0))

#Longest Palindromic subsequence:
def longest_pal_sub(s,start,end):
    if end<start:
        return 0
    #Base case if the start and the end are equal then its a palindromic character    
    if start==end:
        return 1
    result1=0
    #case1 if the elements is equals 
    if s[start]==s[end]:
       result1= 2+longest_pal_sub(s,start+1,end-1)
    #case2 skip one element from the last
    result2=longest_pal_sub(s,start,end-1)
    #case3 skip one element from the start
    result3 = longest_pal_sub(s,start+1,end)
    return max(result1,result2,result3)

# print(longest_pal_sub('abe',0,len('abe')-1))

#Longest Palindromic Substring
def is_palindrom(s,start,end):
  
    while end>start:
        if s[start]!=s[end]:
            return False
        end-=1
        start+=1    
    return True        



def longest_pal_substring(s,start,end):
    if end<start:
        return 0
    if start==end:
        return 1
    result1=0
    #if we have two equals chars then we have to check if the substring 
    # between them is palindrom then we can add them to the sum
    if s[start]==s[end]:
        if(is_palindrom(s,start+1,end-1)==True):
            pal_substring= end-start-1
            result1= 2+pal_substring
    result2=longest_pal_substring(s,start+1,end)
    result3=longest_pal_substring(s,start,end-1)
    return max(result1,result2,result3)

# s=('MQADASM')
# print(longest_pal_substring(s,0,6))

#min cost to reach the end of Array
def min_cost_reach_end(matrix,row,column):
    if row==-1 or column==-1:
        return float('inf')
     
    if row==0 and column==0:
        return matrix[0][0]
    path1=min_cost_reach_end(matrix,row-1,column)+matrix[row][column]
    path2=min_cost_reach_end(matrix,row,column-1)+matrix[row][column]
    return min(path1,path2)   

# matrix=[[4,7,8,6,5],[6,7,3,9,2],[3,8,1,2,4],[7,1,7,3,7],[2,9,8,9,3]]       
# print(min_cost_reach_end(matrix,4,4))
#

#Number of paths to reach last cell with given cost
def num_of_paths(matrix,row,col,cost):
    if cost<0:
        return 0
     
    if   row==0 and col==0:
        return 1 if cost-matrix[row][col]==0 else 0
    if row==0:
        return num_of_paths(matrix,row,col-1,cost-matrix[row][col])     
    if col==0:
        return num_of_paths(matrix,row-1,col,cost-matrix[row][col])      
    path1=num_of_paths(matrix,row-1,col,cost-matrix[row][col])
    path2=num_of_paths(matrix,row,col-1,cost-matrix[row][col])
    return path1+path2

# matrix=[
# [4,7,1,6],
# [5,7,3,9],
# [3,2,1,2],
# [7,1,6,3]
# ]       
# print(num_of_paths(matrix,3,3,25))
 #__________________________________________________________________________________________#

 #### Dynamic programming

 #Fibonacci Series bottom up dynaic programming:

def fib_bottom_up(n):
    memorize=[0]*(n+1)
    memorize[1]=1
    for i in range(2,n+1):
        memorize[i]=memorize[i-1]+memorize[i-2]
    return memorize[n]    
# print( fib_bottom_up(8))

#### number factor top down dynamic programmingd
def ways_get_n(n):
    dp = [0] * (n+1)
    return top_down_ways_get_n(n,dp)

def  top_down_ways_get_n(n,dp):
    
    if  n == 0 or n == 1 or n == 2:
        return 1
    if n == 3:
        return 2
    if dp[n] == 0:
        dp[n]= top_down_ways_get_n(n-1 , dp)+top_down_ways_get_n(n-3 , dp) +top_down_ways_get_n(n-4,dp)
    return dp[n]

def bottom_up_ways_to_get_n(n):
    dp=[0] * (n+1)
    dp[0] = dp[1]=dp[2]=1
    dp[3] = 2
    for i in range(4,n+1):
        dp[i]=dp[i-1]+dp[i-3]+dp[i-4]
    return dp[n]
# print(bottom_up_ways_to_get_n(60))    

#house theif 

def top_down_max_money(house_worth,current,dp):
    if current >= len(house_worth):
        return 0
    if dp[current] == 0 :
        steal_current = house_worth[current] + top_down_max_money(house_worth,current+2,dp) 
        steal_skip = top_down_max_money(house_worth,current+1,dp)
        dp[current] = max(steal_current,steal_skip)
    return dp[current]         
# house_worth = [4,6,20,1,5,10]
# dp=[0] * (len(house_worth)+1)
# print(top_down_max_money(house_worth,0,dp))
def bottom_up_max_money(house_worth):
    dp = [0] * (len(house_worth)+2)
    for i in range(len(house_worth)-1,-1,-1):
        dp[i] = max(house_worth[i]+dp[i+2],dp[i+1])
    return dp[0]    

# house_worth = [4,6,20,1,5,10]
# print(bottom_up_max_money(house_worth))