def solution(arr):
    result = [0,0]
    length = len(arr)
    
    def divide_conquer(r,c,l):
        start_value = arr[r][c]
        for i in range(r,r+l):
            for j in range(c,c+l):
                if arr[i][j] != start_value:
                    l = l//2
                    divide_conquer(r,c,l)
                    divide_conquer(r+l,c,l)
                    divide_conquer(r,c+l,l)
                    divide_conquer(r+l,c+l,l)
                    return
        result[start_value]+=1
            
    divide_conquer(0,0,length)
    return result