class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next


class SinglyLinkedlist:
    def __init__(self, head=None):
        self.head = head

    def InsertAtEnd(self, data):
        temp = Node(data)
        if self.head != None:
            t1 = self.head
            while t1.next != None:
                t1 = t1.next
            t1.next = temp

        else:
            self.head = temp

    def InsertAtBeginning(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def Display(self):
        temp = self.head
        if self.head != None:
            while temp != None:
                print(temp.data)
                temp = temp.next

        else:
            print("List is empty")

    def InsertAfterPosition(self, data, x):
        value = Node(data)
        temp = self.head
        while temp is not None and temp.data != x:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        value.next = temp.next
        temp.next = value

    def Deletell(self, x: int):
        temp=self.head
        prev=None
        if self.head is Node:
            print("The list is Empty")

        if temp is not None and temp.data!=x:
            prev=temp
            temp=temp.next

        if temp==None or prev==None:
            print("value not found")
            return

        else:
            prev.next=temp.next

        
list1 = SinglyLinkedlist()
list1.InsertAtEnd(10)
list1.InsertAtEnd(20)
list1.InsertAtEnd(30)

list1.InsertAfterPosition(25, 20)

list1.Display()