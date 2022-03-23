# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mergeTrees(self, root1, root2):
        if not root1 and not root2:
            return
        elif not root1:
            return root2
        elif not root2:
            return root1

        # 조건문을 다 통과하여 두개의 트리가 존재한다면 value를 합쳐준다.
        root1.val = root1.val + root2.val

        # 각 각의 left, right를 root노드로 넣어서 재귀호출을 이용하여 value를 합쳐준다.
        # 값이 없다면 조건문을 통하여 null이나 None이 들어가게 된다.
        # 재귀를 이용하였기 때문에 리턴 순서는 리프에서 루트까지 역방향으로 값이 반환된다.
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        # 최종적으로는 병합이 모두 끝난 이진트리의 루트 노드인 root1이 반환된다.
        return root1