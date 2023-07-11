# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        q = collections.deque([root])

        while q:
            node = q.popleft()

            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                q.append(node.left)
            
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                q.append(node.right)
        
        ans = list()
        visit = set([target])
        q = collections.deque([(target, 0)])

        while q:
            node, dist = q.popleft()

            if dist == k:
                ans.append(node.val)
            else:
                for edge in graph[node]:
                    if edge not in visit:
                        visit.add(edge)
                        q.append((edge, dist+1))
        return ans

# Time Complexity: O(N)-build graph + O(N)-worst when process whole tree = O(2N) = O(N)
# Space Complexity: O(N) + O(N) = O(N)
