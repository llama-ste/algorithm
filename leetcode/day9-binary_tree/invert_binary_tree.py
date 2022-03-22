# left, right로 부모 자식노드가 연결되어있다.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 아래는 트리를 만드는 함수이다.
def make_tree(lst, idx):
    parent = None

    if idx < len(lst):
        value = lst[idx]
        if value is None:
            return

        parent = TreeNode(value)
        parent.left = make_tree(lst, 2 * idx + 1)
        parent.right = make_tree(lst, 2 * idx + 2)

    return parent


pre_input = make_tree([4,2,7,1,3,6,9], 0)


class Solution:
    def invertTree(self, root):
        if not root:
            return []

        stack = [root]

        while stack:
            node = stack.pop()

            # 한라인에서 두개를 같이 변경하여야 한다.
            node.left, node.right = node.right, node.left

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root

sol = Solution()

print(sol.invertTree(pre_input).left.val)