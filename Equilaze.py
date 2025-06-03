def solve():
    n = int(input())
    a = set(map(int, input().split()))

    a = sorted(a)

    ans, pnt = 0, 0
    for i, val in enumerate(a):
        while val - a[pnt] >= n:
            pnt += 1
        ans = max(ans, i - pnt + 1)

    print(ans)

for _ in range(int(input())):
    solve()
    
# TC: O(n log n), SC: O(n)