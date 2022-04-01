from collections import deque

def check_distance(place, row, col, distance):
    deq = deque()
    deq.append([row,col,distance])
    visited = [[False]*5 for i in range(5)]
    arrow = {0:[1,0], 1:[0,1], 2:[-1,0], 3:[0,-1]}
    visited[row][col] = True
    
    while deq:
        r,c,d = deq.popleft()
        visited[r][c] = True
        for i in range(4):
            nx = r + arrow[i][0]
            ny = c + arrow[i][1]
            nd = d+1
            if 0 <= nx < 5 and 0<=ny<5 and not visited[nx][ny]:
                if place[nx][ny] == 'O' and nd == 1:
                    deq.append([nx,ny,nd])
                if place[nx][ny]=='P' and nd <= 2:
                    return False
    return True
                
def solution(places):
    answer = []
    for place in places:
        flag = 1
        for row in range(5):
            for col in range(5):
                if place[row][col] == "P":
                    if not check_distance(place, row,col,0):
                        flag = 0
        answer.append(flag)
    return answer