class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0
        # print('init', self.snaps, self.snap_id)

    def set(self, index: int, val: int) -> None:
        snap = self.snaps[index][-1]
        if snap[0] == self.snap_id:
            snap[1] = val
        else:
            self.snaps[index].append([self.snap_id, val])
        # print('set', self.snaps, self.snap_id)

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        # print('snap', self.snaps, self.snap_id)

    def get(self, index: int, snap_id: int) -> int:
        # print('get', self.snaps, self.snap_id)
        i = bisect_left(self.snaps[index], [snap_id + 1]) - 1
        return self.snaps[index][i][1]
