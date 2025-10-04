graph={
    'M':['N','Q','R'],
    'N':['O','Q','M'],
    'R':['M'],
    'O':['P','N'],
    'Q':['M','N'],
    'P':['O','Q']
    }
def dfs(g,n,seen,d):
    if n not in seen:
        seen.append(n)
        for i in g[n]:
            if seen[-1] is d:
                break
            dfs(g,i,seen,d)
    return seen

print(dfs(graph,'M',[],'R'))