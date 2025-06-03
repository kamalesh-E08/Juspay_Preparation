t = int(input()) 
for  _ in range(t):
    n = int(input()) 
    lis = []
    lis.append(list(input())) 
    lis.append(list(input()))
    cnt = 0 
    for row in range(2):
        for col in range(1,n-1):
            if row == 0:
                if lis[row][col] == "." and lis[row][col-1]=="." and lis[row][col+1] == "." and lis[row+1][col] == "." and lis[row+1][col-1] == "x" and lis[row+1][col+1] == "x":
                      cnt+=1 
            else:
                if lis[row][col] == "." and lis[row][col-1]=="." and lis[row][col+1] == "." and lis[row-1][col] == "." and lis[row-1][col-1] == "x" and lis[row-1][col+1] == "x":
                      cnt+=1
    print(cnt)
    
# TC: O(n), SC: O(1)