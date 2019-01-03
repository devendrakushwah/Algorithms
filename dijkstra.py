INF=9999
def single_source_shortest_path(G,S,n):
  #G->Graph S->Source n->no. of nodes
  dist=G[S][:] #assigning the initial values of distance of S to every other node
  visited=[False]*n #initially no node is visited

  visited[S]=True #set S as visited

  for i in range(n):
    if((not visited[i]) and (i!=S) ):
      visited[i]=True
      for j in range(n):
        dist[j]=min(dist[j],dist[i]+G[i][j])
    i=0
  return dist

#Driver
G=[[0,INF,12,10],
   [5,0,INF,INF],
   [INF,INF,0,13],
   [INF,6,INF,0]]
path=(single_source_shortest_path(G,3,4))
print(path)
  
  
