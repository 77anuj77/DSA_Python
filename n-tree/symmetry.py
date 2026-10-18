class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return 
        
        left_queue=[]
        right_queue=[]

        left_queue.append(root.left)
        right_queue.append(root.right)

        while left_queue and right_queue:
            left_root=left_queue.pop(0)
            right_root=right_queue.pop(0)
            

            if left_root is None and right_root is None:
                continue
            if left_root is None or right_root is None:
                return False
            
            if  left_root.val != right_root.val:
                return False

            left_queue.append(left_root.left)
            right_queue.append(right_root.right)

            left_queue.append(left_root.right)
            right_queue.append(right_root.left)
        
        return True