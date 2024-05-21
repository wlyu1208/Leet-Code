class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        stack = [(0, [0])]

        while stack:
            current_node, path = stack.pop()

            if current_node == len(graph) - 1:
                paths.append(path)
            
            for _next in graph[current_node]:
                stack.append((_next, path + [_next]))

        return paths
