s = input()
lst = [-1]
for i in range(len(s)):
    if s[i] == 'y':
        lst.append(i)
        
lst.append(len(s))
if len(lst) == 0 or len(lst) == len(s):
    print(0)
else:
    A = []
    for i in range(1, len(lst)):
        diff = lst[i] - lst[i-1] - 1
        A.append(diff)

    print(sum(A) - min(A))

# TC:O(n), SC:O(n)