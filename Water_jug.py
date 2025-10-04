def water_jug_manual_path():
    #(Jug1,Jug2)
    steps=[]

    #Step 1:(0,0)
    a,b=0,0
    steps.append((a,b))

    #Step 2:Fill the Jug 1(5,0)
    a=5
    steps.append((a,b))

    #Step 3:Pour Jug1,Jug2(1,4)
    transfer=min(5,4-b) #5 can give 4
    a-=transfer #a=a-transfer
    b+=transfer #b=b+transfer
    steps.append((a,b))

    #step 4:Empty Jug2(1,0)
    b=0
    steps.append((a,b))

    #Step 5:Pour Jug1,Jug2(0,1)
    transfer=min(a,4-b) #1 can go into empty 4L jug
    a-=transfer
    b+=transfer
    steps.append((a,b))

    #Step 6:Fill Jug 1(5,1)
    a=5
    steps.append((a,b))

    #Step 7:Pour Jug 1,Jug 2(2,4)
    transfer=min(a,4-b) #Only 3 can go into 3 remaining in Jug 2
    a-=transfer
    b+=transfer
    steps.append((a,b))

    #Step 8:Empty Jug 2 ->(2,0) Goal Reached
    b=0
    steps.append((a,b))

    #Print
    print("Steps to reach(2,0): ")
    for idx,state in enumerate(steps):
        print(f"Step {idx}: Jug1={state[0]}L,Jug2={state[1]}L")

water_jug_manual_path()