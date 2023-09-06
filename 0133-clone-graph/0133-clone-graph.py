"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        q, track = deque([node]), {node.val: Node(node.val, [])}

        while q:
            cur = q.popleft()
            cur_track = track[cur.val]

            for _next in cur.neighbors:
                if _next.val not in track:
                    track[_next.val] = Node(_next.val, [])
                    q.append(_next)
                cur_track.neighbors.append(track[_next.val])
        return track[node.val]