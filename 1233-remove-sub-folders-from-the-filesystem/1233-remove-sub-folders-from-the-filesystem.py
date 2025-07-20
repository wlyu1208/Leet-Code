class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        _set = set(folder)
        answer = []

        for f in folder:
            is_sub = False
            path = []
            for part in f.split('/')[1:]:
                path.append(part)
                parent = "/"+"/".join(path[:-1])
                if len(path) > 1 and parent in _set:
                    is_sub = True
                    break
            if not is_sub:
                answer.append(f)
        return answer