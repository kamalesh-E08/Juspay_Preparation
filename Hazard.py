from collections import defaultdict

n, m = map(int, input().split())
A = list(map(int, input().split()))
adj = defaultdict(list)

for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    
ans = 0
stack = [(1, 0)]
vis = [0]*(n)

while stack:
    v, c = stack.pop()
    if vis[v-1]:
        continue
    
    vis[v-1] = 1
    if A[v-1] == 1:
        c+=1
    else:
        c = 0
    
    if c>m:
        continue
    if v!=1 and len(adj[v])==1:
        ans += 1
    else:
        for u in adj[v]:
            if not vis[u-1]:
                stack.append((u, c))
        
print(ans)

# TC: O(n), SC: O(n)