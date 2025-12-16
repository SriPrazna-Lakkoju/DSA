# definition of a node
class node:
    def __init__(self,data):
        self.data = data
        self.next = none

#singly linked list:
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)

temp = head
while temp is not None :
    print(temp.data,end=" ")
    temp=temp.next
