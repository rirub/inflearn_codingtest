def DFS(L,s):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt +=1
        return
    else:
       for i in range(s,n+1):
            res[L]=i
            DFS(L+1, i+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    res = [0] * m
    DFS(0,1)
    print(cnt)