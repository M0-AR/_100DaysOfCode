# Global variables, I intentionally leave the values as ... because # I don't have any meaningful values yet. But it won't affect how
# you understand the problem, I promise.
R, C = ...
m = ...
sr, sc = ...
rq, cq = ...
# Variables used to keep track of total number of steps to be taken
move_count = 0
nodes_left_in_layer = 0
nodes_in_next_layer = 1
# Variable to see whether we already reached at the end or not
reached_end = False
# Matrix to keep track of visited cells.
visited = ...
# North, South, East and West direction vectors
dr = [-1, +1, 0, 0]
dc = [0, 0, +1, -1]

def solve():
    rq.enqueue(sr)
    cq.enqueue(sc)
    visited[sr][sc] = True

    while rq.size() > 0:
        r = rq.dequeue()
        c = cq.dequeue()
        if m[r][c] == 'E':
            reached_end = True
            break
        explore_neighbors(r, c)
        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1
    if reached_end == True:
        return move_count
    return -1

def explore_neighbors(r, c):
    for i in 4:
        rr = r + dr[i]
        cc = c + dc[i]

        if rr < 0 or cc < 0:
            continue
        if rr >= R or cc >= C:
            continue

        if visited[r][c] == True:
            continue
        if m[r][c] == '#':
            continue

        rq.enqueue(rr)
        cq.enqueue(cc)
        visited[r][c] =True

        nodes_in_next_layer += 1