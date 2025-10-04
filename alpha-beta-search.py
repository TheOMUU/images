tree={
    'A':['B','C'],
    'B':[3,5],
    'C':[6,9]
}

def minimax_alpha_beta(node,depth,alpha,beta,max_player):
    if depth==0:
        if node in tree:
            return tree[node][0] if max_player else tree[node][0]
        else:
            return node

    if max_player:
        value=float('-inf')
        for child in tree[node]:
            value=max(value,minimax_alpha_beta(child,depth-1,alpha,beta,False))
            alpha=max(alpha,value)
            if alpha>=beta:
                print(f"Pruning branch at node{node}")
                break
        return value

    else:
        value=float('-inf')
        for child in tree[node]:
            value=max(value,munimax_alpha_beta(child,depth-1,alpha,beta,True))
            beta=min(beta,value)
            if beta<=alpha:
                print(f"Pruning branch at node{node}")
                break
        return value

best_score=minimax_alpha_beta('A',1,float('-inf'),float('inf'),True)
print(f"The best Score is:{best_score}")