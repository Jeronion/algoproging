from typing import Iterable, Optional, List
from collections import deque

# https://informatics.msk.ru/mod/statements/view.php?id=11576#1
"""
array: map[int] = list(map(int, input().split()))[:-1]
root = build_tree(array)
print(getDepth(root))
"""

# https://informatics.msk.ru/mod/statements/view.php?id=11576&chapterid=761#1
"""
array = list(map(int, input().split()))[:-1]
root = build_tree(array)
print_leaves(root)
"""
# https://informatics.msk.ru/mod/statements/view.php?id=11576&chapterid=759#1
"""
array = list(map(int, input().split()))[:-1]
root = build_tree(array, dubs=False)
print(get_second_max(root))
"""

# https://informatics.msk.ru/mod/statements/view.php?id=11576&chapterid=757#1
"""
array = list(map(int, input().split()))[:-1]
root = build_tree(array, dubs=False)
print_ones(root)
"""

# https://informatics.msk.ru/mod/statements/view.php?id=11576&chapterid=760#1
"""
array = list(map(int, input().split()))[:-1]
root = build_tree(array, dubs=False)
inorder(root)
"""

# 
"""
array = list(map(int, input().split()))[:-1]
root = build_tree(array, dubs=False)
print("YES" if is_balanced(root) else "NO")
"""

class Node:
    __slots__  = ["key", "left", "right"]
    
    def __init__(self, key: int) -> None:
        self.key = key
        self.left = None
        self.right = None


def insert_r(root: Node, key: int, dubs: bool=False) -> Node:
    if root is None:
        return Node(key)
    elif key < root.key:
        root.left = insert_r(root.left, key)
    else:
        if not (not dubs and key == root.key):
            root.right = insert_r(root.right, key)
    return root

def insert_i(root: Node, key: int, dubs: bool=False) -> Node:
    if root is None:
        return Node(key)
    dummy = root
    while True:
        if key < dummy.key:
            if dummy.left is None:
                dummy.left = Node(key)
                break
            dummy = dummy.left
        else:
            if not dubs and key == dummy.key:
                break
            if dummy.right is None:
                dummy.right = Node(key)
                break
            dummy = dummy.right
    return root

def search_BST(root: Node, key: int) -> bool:
    # for BST only
    present = False

    while root is not None:
        if root.data == key:
            present = True
            break
        elif key > root.data:
            root = root.right
        else:
            root = root.left

    return present




def delete(root: Node | None, key: int) -> Node | None:
    if root is None:
        return None

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None and root.right is None:
            return None
        
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        max_left = root.left
        while max_left.right:
            max_left = max_left.right
        
        root.key = max_left.key
        
        root.left = delete(root.left, max_left.key)

    return root

def getDepth(root: Node) -> int:
    if root is None:
        return 0
    return max(getDepth(root.left), getDepth(root.right)) + 1


def inorder_r(root: Node) -> None:
    if root:
        inorder_r(root.left)
        print(root.key, end=" ")
        inorder_r(root.right)

def preorder_r(root: Node) -> None:
    if root:
        print(root.key, end=" ")
        preorder_r(root.left)
        preorder_r(root.right)

def postorder_r(root: Node) -> None:
    if root:
        postorder_r(root.left)
        postorder_r(root.right)
        print(root.key, end=" ")

def levelOrderRec(root: Node, level: int, res: list[list]) -> None:
    if root:
        if len(res) <= level:
            res.append([])

        res[level].append(root.data)

        levelOrderRec(root.left, level + 1, res)
        levelOrderRec(root.right, level + 1, res)

def levelOrder(root: Node) -> list[list]:
    res = []
    levelOrderRec(root, 0, res)
    return res

def preorder_i(root: Node) -> List[int]:
    res = []

    if not root:
        return res
        
    st = [root]

    while st:
        node = st.pop()
        res.append(node.key)

        if node.right:
            st.append(node.right)
            
        if node.left:
            st.append(node.left)
        
    return res

def inorder_i(root: Node) -> List[int]:
    res = []
    stack = []
    node = root

    while stack or node:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        res.append(node.key)

        node = node.right

    return res

def postorder_i(root: Node) -> List[int]:
    res = []
    stack = []
    node = root
    last_visited = None

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            peek = stack[-1]
            if peek.right and last_visited != peek.right:
                node = peek.right
            else:
                res.append(peek.key)
                last_visited = stack.pop()

    return res


def print_leaves(root: Node) -> None:
    if root.left:
        print_leaves(root.left)
    if root.right:
        print_leaves(root.right)
    if not root.right and not root.left:
        print(root.key)

def print_full(root: Node) -> None:
    if root.left:
        print_full(root.left)
    if root.right and root.left:
        print(root.key)
    if root.right:
        print_full(root.right)

def print_ones(root: Node) -> None:
    if root.left:
        print_ones(root.left)
    if (root.left or root.right) and not (root.left and root.right):
        print(root.key)
    if root.right:
        print_ones(root.right)


def get_max(root: Node) -> int:
    dummy = root
    while dummy.right:
        dummy = dummy.right
    return dummy.key

def get_second_max(root: Node) -> int:
    if root is None:
        return None
    
    dummy = root
    parent = None

    while dummy.right:
        parent = dummy
        dummy = dummy.right

    if dummy.left:
        dummy = dummy.left
        while dummy.right:
            dummy = dummy.right
        return dummy.key

    if parent:
        return parent.key
    return None


def is_balanced(root: Node) -> bool:
    def height(node):
        if node is None:
            return 0
        
        left = height(node.left)
        if left == -1:
            return -1
        
        right = height(node.right)
        if right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1

    return height(root) != -1


def getLevel(root: Node, target: int, level: int) -> int:
    if root is None:
        return -1
    
    if root.key == target:
        return level

    leftLevel = getLevel(root.left, target, level + 1)
    if leftLevel != -1:
        return leftLevel

    return getLevel(root.right, target, level + 1)

def search(root: Node, target: int) -> Node:
    # for all trees
    if root is None:
        return None
    
    if root.key == target:
        return root
    
    left = search(root.left, target)
    if left is not None:
        return left

    return search(root.right, target)

def search_parent(root: Node, target: Node, parent) -> Node:
    # for all trees
    if root is None:
        return None
    
    if target == root.key:
        return parent

    left = search_parent(root.left, target, root.key)
    if left is not None:
        return left
    
    return search_parent(root.right, target, root.key)


def InsertNode(root, data):
    # for all trees
    if root is None:
        root = Node(data)
        return root

    q = deque()
    q.append(root)

    while q:
        curr = q.popleft()

        if curr.left is not None:
            q.append(curr.left)
        else:
            curr.left = Node(data)
            return root

        if curr.right is not None:
            q.append(curr.right)
        else:
            curr.right = Node(data)
            return root


def build_tree(elements: Iterable, dubs: bool=False) -> Node:
    root: None = None
    for key in elements:
        root: Node = insert_i(root, key, dubs=dubs)
    return root


class TreeNode:
    __slots__  = ["val", "left", "right"]
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# LeetCode
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root: Optional[TreeNode]) -> None:
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        
        inorder(root)
        return res
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False

        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        
        if left is None or right is None:
            return False
        
        if left.val != right.val:
            return False
        
        return self.isMirror(left.right, right.left) and self.isMirror(left.left, right.right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)
    
    def getDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.getDepth(root.left), self.getDepth(root.right)) + 1

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(left, right):
            if left > right:
                return

            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = buildTree(left, mid - 1)
            node.right = buildTree(mid + 1, right)
            return node

        return buildTree(0, len(nums) - 1)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right,targetSum)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, path, cur_sum):
            if not node: 
                return
            
            cur_sum += node.val
            path.append(node.val)

            if not node.left and not node.right and cur_sum == targetSum:
                res.append(path[:])
            
            dfs(node.left, path, cur_sum)
            dfs(node.right, path, cur_sum)
            
            path.pop()
        
        dfs(root, [], 0)
        return res

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        stack = []

        for _ in range(k):
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            res = root.val
            root = root.right

        return res


def main():
    ...
    
if __name__ == "__main__":
    main()