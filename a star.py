graph = { 
    "S" : ({"A":5,"B":4},10),
    "A":({"C":6,"D":8},8),
    "B":({"E":2,"G":3},2),
    "C":({},4),
    "D":({"G":4},5),
    "E":({},6),
    "G":({},0)
}

def get_min(q):
    mn = (0, (0, float("INF")))
    for i in q:
        if sum(q[i] , sum(mn[1])):
            mn = (i, q[i])
            # print(mn)
    return mn[0]
def a_star(graph, prev, dst, path, pcost, q):
    # n : (h(n), g(n)) of current vertex
    print("connected nodes of current node ", prev, " with h(n) values : ") # and
    for n in graph[prev][0]: # neighbours list n = Z, S, T
        if n not in path:
            q[n] = (graph[n][1], graph[prev][0][n])
            print(n, "->", q[n])
            add1 = sum(q[n])
            path_cost = pcost + add1 # a to c = a + b ?? b to c?? tot a* value
            print("a* value for ", n, " is : ", path_cost)
    while q:
        mn = get_min(q)
        print("selecting minimum vertex : ", mn)
        print("_____________________")
        if dst == mn:
            return path + [dst]
        pc = pcost + q[mn][1]
        print("previous path cost : ", pc)
        # del q[mn]
        new_path = a_star(graph, mn, dst, path + [mn], pc, q)
        if new_path:
            return new_path
    return []
source = input("enter source vertex : ")

dest = input("enter destination vertex : ")
heuristic = int(input("enter given heuristic value for source : "))
path = a_star(graph, source, dest, [], 0, {source : (heuristic, 0)})
if path:
    print(path)
else:
    print("path not found!")
##print("->".join(a_star(graph, "S", "G", [], 0, {"S" : (399, 0)})))