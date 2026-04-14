"""
BST is a type of tree has two restrictions:
    Value of left child of any node < Value of the current node.
    Value of the current node < Value of its right node.

The above two restrictions are applicable for the whole tree not just any branch.

Search is O(h) times - h is the height of the tree.

Balanced binary search tree:
    All restriction of BST.
    Height balanced. h = O(logN) implies search is O(logN)

There is no scope for equality in BST. That's why in a BST there are no duplicates.

Set data structure is implemented using Balanced BST.

Height balanced tree types:
    Red black tree
    AVL Tree

To insert in a BST, first find the position to place the node. Start from the top if the
value is greater than the root, then we need to go to the right branch else left branch.
Repeat the same in the right branch until you find the right place for new Node.

Inorder successor: Node that comes next in the inorder traversal.
                   Eg: 3 5 7 8 9 10 11 12 15 19
                   IS(9) = 10  IS(3) = 5 IS(12) = 15

Inorder predecessor: Node that comes before in the inorder traversal.
                    IP(9) = 8 IP(12) = 11

3 cases in deletion:
    When node doesn't have children - the simplest case. To delete this node,
                                      modify its parent and set its child to null.

    When node has one child - Attach this node's child to its parent as its child and
                              delete this node.

    When node has two children - Instead of deleting the node, We will find the inorder
                                 successor of that node, swap the IS node and this node.
                                 We will recursively call delete of that node, in this case
                                 either that node which took the place of IS node will have no children or
                                 single child which can be deleted easily.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class KthSmallestBST:
    def __init__(self):
        self.count = None
        self.k = None
        self.ans = None

    def kthSmallest(self, root, k: int) -> int:
        self.k = k
        self.count = 0
        self.inorder(root)
        return self.ans

    def inorder(self, node):
        if node.left is not None:
            self.inorder(node.left)
        self.count += 1
        if self.count == self.k:
            self.ans = node.val
            return
        if node.right is not None:
            self.inorder(node.right)


node = TreeNode(5)
node.left = TreeNode(3)
node.right = TreeNode(6)
node.left.left = TreeNode(2)
node.left.right = TreeNode(4)
node.left.left.left = TreeNode(1)


# print(KthSmallestBST().kthSmallest(node, 3))


class ValidBST:
    def isValidBST(self, root) -> bool:
        return self.isValidSubTree(root, -(1 << 31), (1 << 31) - 1)

    def isValidSubTree(self, node, lower, higher):
        if node is None:
            return True
        elif node.val < lower or node.val > higher:
            return False
        else:
            return self.isValidSubTree(node.left, lower, node.val - 1) and self.isValidSubTree(node.right, node.val + 1,
                                                                                               higher)


# print(ValidBST().isValidBST(node))


class LowestCommonAncestorBST:
    """
    Lowest Common ancestor of any two nodes is a node that is the common ancestor of both the nodes
    and of the lowest value.

    If one of the nodes is already the ancestor of the other node, then that node can be
    considered ancestor of itself.

    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
