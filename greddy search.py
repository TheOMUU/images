graph={
    'F':({'C':8,'D':14},0),
    'E':({'B':11,'C':11},10),
    'D':({'A':5,'C':6,'F':14},5),
    'C':({'A':12,'E':11,'F':8},5),
    'B':({'A':10,'E':11},15),
    'A':({'B':10,'C':12,'D':5},10)
    }

def greedy_search_rec(graph,prev,dst,path,q):
    #n=(h(n))
    print("Connected nodes of current node",prev,"with h(n) values: ")
    for n in graph[prev][0]:        #neighbours list prev=arad,->Z,S,T
        if n not in path:
            q[n]=graph[n][1]    #n=Z    [1]=374
            print(n,"->",q[n])
    while q:
        mn=min(q,key=q.get)
        print("Taking minimum h(n) vertext: ",mn)
        #print(mn)
        if dst==mn:
            return path+[dst]
        #del q[mn]
        new_path=greedy_search_rec(graph,mn,dst,path+[mn],q)
        if new_path:
            return new_path
    return[]

#source=input("Enter the source vertext: ")
#dest=input("Enter the Destination vertext: ")
#path=greedy_search_rec(graph,source,dest,[source],{})
#if path:
#   print(path)
#else:
#   print("Path not found!")

print("Greedy Search Recursive: ","->"
      .join(greedy_search_rec(graph,"A","F",["A"],{}))
          or "Path not found")