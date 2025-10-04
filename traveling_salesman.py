import random

#Distance for 4 cities
distance=[
    [0,2,9,10],
    [2,0,6,4],
    [9,6,0,3],
    [10,4,3,0]
]

#total distance of a tour
def get_cost(tour):
    cost=0
    for i in range(len(tour)):
        cost +=distance[tour[i-1]][tour[i]]
        #print("Cost of tour",cost)
    return cost

#new tour by swaaping two cities
def get_neighbor(tour):
    a,b=random.sample(range(len(tour)),2)
    tour[a],tour[b]=tour[b],tour[a]
    return tour

def hill_climb():
    current=[0,1,2,3]
    random.shuffle(current)
    current_cost=get_cost(current)

    print("Startin tour: ",current,"Cost:",current_cost)

    for i in range(10):
        neighbor=current[:]
        #print("Current neighbor: ",neighbor)
        neighbor=get_neighbor(neighbor)
       #print("Connected neighbor: ",neighbor)
        neighbor_cost=get_cost(neighbor)

        if neighbor_cost<current_cost:
            current=neighbor
            #print("Current neighbor: ",neighbor)
            current_cost=neighbor_cost
            #print("Current Cost: ",current_cost)

            print("Better tour found: ",current,"Cost: ",current_cost)

    return current,current_cost

best_tour,best_cost=hill_climb()
print("\nBest tour: ",best_tour)
print("Best Cost: ",best_cost)