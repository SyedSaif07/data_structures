"""
Tree are hierarchical data structure. In real world, trees have many practical applications.

Eg: CEO is top level. Below CEO there are CFO, CTO, CMO. Below each of these there are
VPs. Below VPs there Engineering Managers.

Types:
    Rooted tree: There is a special node called root which acts as the starting point of
                 the tree.

    Non rooted tree: There is no concept of root. Every node is equal.
                     Eg: A connected to B. A connected to C. B connected to D. D connected to E.
                     Non rooted trees are handled by graph algorithm.

Terms related to trees:
    root node: top level node - CEO

    leaf node: a node which does not have children.

    children: child of a node is the direct descendant of the node.
              Eg: CFO,CTO,CMO are the children nodes of CEO.

    parent: CTO is the parent node of VP node.

    siblings: nodes which have the same parent. VP1 VP2 are siblings as their parent is CTO.

    cousin: cousin nodes have their parents as siblings. EM1 and EM3 are cousins since VP1 and VP2 are siblings.

    internal: a node which is not a leaf node.

    level: level of the node = distance of the node from the root + 1
           level of the node = level of parent + 1

    height: distance of the node from the farthest leaf node in its subtree + 1
            subtree is a tree under the node.

    height of a tree: height of the root node.

    height of any node: max(height(node.left), height(node.right)) + 1

Tree traversal:
    Pre-order traversal: Current node - Left subtree - Right subtree
                         Eg: A,B, D, E, H, I, C, F, G
                         Use this for problems when you need information from the parent.

    Post-order traversal: Left subtree - Right subtree - Current node
                          Eg: D, E, H, I, B, F, G, C, A
                          Use this for problems when you need information from the children.

    In-order traversal: Left subtree - Current node - Right subtree
                        Eg: D, B, E, H, I, A, F, C, G
                        Problems involving binary search tree.

    Level order traversal: Traversing a tree level by level. Start from level 1 and process
                           all the nodes from left to right and move to level 2, process all the nodes.
                           Repeat this for all levels.
                           Eg: A, B, C, E, F, D, K, G, H, L, I, M

    Reverse level order traversal: Traversing level by level but process the nodes from right to
                                   left.
                                   Eg: A, C, B, K, D, F, E, I, L, H, G, M


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InOrderTraversal:
    def __init__(self):
        self.ans = []

    def inorderTraversal(self, root):
        self.inorder(root)
        return self.ans

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            self.ans.append(node.val)
            self.inorder(node.right)


class LevelOrderTraversal:
    def levelOrder(self, root):
        ans = []
        if not root:
            return ans
        from collections import deque
        q = deque()
        q.append((root, 1))

        while len(q) > 0:
            (node, level) = q[0]
            q.popleft()
            if len(ans) < level:
                ans.append([])
            ans[-1].append(node.val)

            if node.left is not None:
                q.append((node.left, level + 1))
            if node.right is not None:
                q.append((node.right, level + 1))
        return ans


class SameTree:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


class SymmetricTree:
    def isSymmetric(self, root):
        return self.isSym(root.left, root.right)

    def isSym(self, f1, f2):
        if f1 is None and f2 is None:
            return True
        elif f1 is None or f2 is None:
            return False
        else:
            return f1.val == f2.val and self.isSym(f1.left, f2.right) and self.isSym(f1.right, f2.left)
