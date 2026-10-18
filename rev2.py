class Node:
    def __init__(self,next, val=None):
        self.val= val
        self.next=next

class Best_sort:

    def __init__(self):
        pass

    def Merge_sort(self, head):

        def Merge_sorted(left, right):
            result= Node()
            temp= result

            while left is not None and right is not None:
                if left.val<=right.val:
                    temp.next= left.val
                    left= left.next

                else:
                    temp.next=right.val
                    right=right.next

            if right:
                temp.next=right
            if left:
                temp.next=left

            return result


        def merge(head):
            if head is None or head.next is None:
                return head

            slow, fast= head, head.next

            while fast and fast.next:
                slow= slow.next
                fast= fast.next.next

            right=slow.next
            slow.next=None

            left= merge(head)
            right= merge(right)

            return Merge_sorted(left, right)
        
head= Node(2)
head.next= Node(5)
head.next.next= Node(4)
head.next.next.next= Node(6)
head.next.next.next.next=Node(3)

obj= Best_sort()
print(obj.Merge_sort(head))

temp=head
while temp is not None:
    print(f"{temp.val}")
    temp=temp.next
