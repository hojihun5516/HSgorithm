def solution(triangle):
    new_tri = [[0]]
    new_tri[0][0] = triangle[0][0]
    
    for row_index, tri in enumerate(triangle[1:]):
        len_tri = len(tri)
        temp_arr = []
        for col_index,col in enumerate(tri):
            if col_index == 0:
                temp_arr.append(new_tri[row_index][col_index] + col)
            elif col_index == len_tri-1:
                temp_arr.append(new_tri[row_index][col_index-1] + col)
            else:
                temp_arr.append(max(new_tri[row_index][col_index-1]+col , new_tri[row_index][col_index]+col))
        new_tri.append(temp_arr)
            
    return max(new_tri[-1])
