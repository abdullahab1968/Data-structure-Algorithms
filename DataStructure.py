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
items_name=['item1','item2','item3','item4','item5','item6']
items_weight=[6,10,3,5,1,3]
items_value=[6,2,1,8,3,5]
items=[]
for i in range(0,len(items_name)):
    items.append(Item(items_name[i],items_value[i],items_weight[i]))

print(fractional_knapsack(items,10))
