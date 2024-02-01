# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def reverse_op(root: TreeNode):
            total = 0
            count = 0
            queue = []
            num_nodes = 0
            if root:
                # First print the data of node
                print(root.val)
                total += root.val
                count += 1

                x, a, i = reverse_op(root.left)
                y, b, j = reverse_op(root.right)

                num_nodes += (x + y)
                total += (a + b)
                count += (i + j)

                average = int(total / count)
                if average == root.val:
                    num_nodes += 1
                else:
                    num_nodes += 0
            return num_nodes, total, count

        ans, _, _ = reverse_op(root)
        return ans



    def averageOfSubtree0(self, root: TreeNode) -> int:
        if root is None:
            return 0
        total = 0
        count = 0
        queue = []
        num_nodes = 0

        # Enqueue Root and initialize height
        queue.append(root)

        while (len(queue) > 0):

            # Print front of queue and
            # remove it from queue
            print(queue[0].val, end=" ")
            total += queue[0].val
            count += 1
            node = queue.pop(0)

            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)
            num_nodes += self.averageOfSubtree(node.left)

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)
            num_nodes += self.averageOfSubtree(node.right)

        average = int(total/count)
        if average == root.val:
            num_nodes += 1
            return num_nodes
        else:
            # num_nodes += 0
            return 0


if __name__ == '__main__':
    # root = [4,8,5,0,1,null,6]
    root = TreeNode(4)
    root.left = TreeNode(8)
    root.right = TreeNode(5)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(6)

    s = Solution()
    num_nodes = s.averageOfSubtree(root)
    pass
