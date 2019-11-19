t=int(input())
for i in range(t):
    v,e=map(int,input().split())
    g=[[0]*0 for i in range(v)]
    l=list(map(int,input().split()))
    for i in range(e):
        (g[l.pop(0)]).append(l.pop(0))
    c=0
    for i in g:
        c+=len(i)
    print(c)
