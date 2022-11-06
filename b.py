N, M = map(int, input().split())

city = [set([]) for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    city[a-1].add(b)
    city[b-1].add(a)

ans = [sorted(list(city[i])) for i in range(N)]

for i in range(N):
    print('{} {}'.format(len(ans[i]), ' '.join(map(str, ans[i]))))