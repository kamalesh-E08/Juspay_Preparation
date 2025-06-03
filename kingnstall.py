n = int(input())
lst = []
end = -1
for _ in range(n):
    lst.append(list(map(int, input().split())))
    if lst[-1][1] > end:
        end = lst[-1][1]

lst.sort()
start = 0
while start <= end:
    dis = (start+end)//2
    path = lst[0][0]
    i = 1
    while i < n:
        f = path + dis
        if f > lst[i][0]:
            end = dis - 1
            break
        else:
            path = max(f, lst[i][0])
        i+=1
    if i == n:
        ans = dis
        start = dis + 1
    
print(ans)

# TC: O(n log m), where m is the maximum distance