class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle_list = [[1]]
        
        for i in range(rowIndex+1):
            cur_list = copy.deepcopy(triangle_list[-1])
            
            if i == 0:
                continue
            elif i == 1:
                cur_list.append(1)
                triangle_list.append(cur_list)            
            else:
                new_list = [1]
                for j in range(1, len(cur_list)):
                    new_list.append(cur_list[j-1] + cur_list[j])
                new_list.append(1)
                triangle_list.append(new_list)
        return triangle_list[-1]
