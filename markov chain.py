state matrix

Transition Matrix



for r in range(0,d):
    result=statematrix
    for i in range(len(statematrix)):
        for j in range(len(transition[0])):
            for k in range(len(transition)):
                product[i][j]=statematrix[i][k]*transition[k][j]+product[i][j]
    for i1 in range(len(product)):
        for j1 in range(len(transition[0])):
            for k1 in range(len(transition)):
                result[i1][j1]=product[i1][k1]*[k1][j1]+transition[i1][j1]
    for r in result:
        print(r)


