# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):

    def __init__(self):
        self.queue = []

    def maxDepth(self, root):
        if root is None:
            return 0

        depth = 0
        self.enqueue(root)
        while len(self.queue) > 0:
            l = len(self.queue)

            for i in range(l):
                node = self.dequeue()
                if node.children:
                    for child in node.children:
                        self.enqueue(child)
            depth += 1
        return depth

    def enqueue(self, root):
        if root is None:
            return

        queue = self.queue
        queue.append(root)

    def dequeue(self):
        v = self.queue[0]
        del self.queue[0]
        return v


# Create tree
root = Node(1)

node3 = Node(3)
node2 = Node(2)
node4 = Node(4)

node5 = Node(5)
node6 = Node(6)

# Connect root
root.children = [node3, node2, node4]

# Connect node 3
node3.children = [node5, node6]

obj = Solution()
print(obj.maxDepth(root))