from collections import deque

goal = '123456780'
moves = {
    0: [1,3],
    1: [0,2,4],
    2: [1,5],
    3: [0,4,6],
    4: [1,3,5,7],
    5: [2,4,8],
    6: [3,7],
    7: [4,6,8],
    8: [5,7]
}

def bfs(start):
    visited = set()
    queue = deque([(start, [])])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]
        if state in visited:
            continue
        visited.add(state)
        zero = state.index('0')
        for move in moves[zero]:
            new_state = list(state)
            new_state[zero], new_state[move] = new_state[move], new_state[zero]
            queue.append((''.join(new_state), path + [state]))
    return None

start = '123405678'
solution = bfs(start)
if solution:
    print("Steps to Solve : ")
    for s in solution:
        print(s[0:3])
        print(s[3:6])
        print(s[6:9])
        print("-------")
else:
    print("No solution found.")