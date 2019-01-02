def all_pair_shortest_path(gph,n):
  A=gph[:]
  for k in range(n):
    for i in range(n):
      for j in range(n):
        A[i][j]=min(A[i][j],A[i][k]+A[k][j])
  return A

#Driver
INF=9999
G=[[0,INF,12,10],
   [5,0,INF,INF],
   [INF,INF,0,13],
   [INF,6,INF,0]]
path=(all_pair_shortest_path(G,4))
print(path[3][2]) #test to print shortest dist between 3&2
