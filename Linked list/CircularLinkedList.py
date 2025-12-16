#circular linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)
head.next.next.next.next=head


temp = head
while True :
    print(temp.data,end=" ")
    temp=temp.next
    if temp!=head:
        print("->",end=" ")
    else:
        break
print()
