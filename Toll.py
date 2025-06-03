from collections import defaultdict
def get_path(x, y):
    path = []
    while x != y:
        if x > y:
            path.append(x)
            x//= 2
        else:
            path.append(y)
            y//= 2
        
    return path


toll = defaultdict(int)
total_toll = 0
n = int(input())
for  _ in range(n):
    q, x, y, t = map(int, input().split())
    path = get_path(x, y)
    if q == 1:
        for p in path:
            toll[p] += t
    else:
        for p in path:
            total_toll += toll[p]

print(total_toll)
        
# TC: O(log n), SC: O(n)