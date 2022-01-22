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

LL1=LinkedList()

LL1.insert_begin(1)
LL1.insert_begin(2)
LL1.insert_begin(3)
LL1.insert_begin(4)
LL1.insert_last(5)
LL1.insert_last(6)
LL1.traversal()
LL1.delete_node(1)
LL1.delete_node(2)
LL1.delete_node(3)
LL1.delete_node(4)
LL1.delete_node(5)
LL1.delete_node(6)
current=LL1.head
LL1.traversal()