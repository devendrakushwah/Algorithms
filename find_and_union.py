N=6 #no of initial components
component=[0]*6

def initialise(n):
  for i in range(n):
    component[i]=i

def find(u):
  return component[u]

def union(u,v):
  temp=component[u]
  for i in range(N):
    if(component[i]==temp):
      component[i]=component[v]
      
