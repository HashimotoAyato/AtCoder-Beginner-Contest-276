import math

N = int(input())
P = list(map(int, input().split()))

K = 1
num_set = set(list(range(1,N+1)))
for i in range(N):
    rank = (sorted(list(num_set)).index(P[i]))
    num_set.remove(P[i])
    K += rank * math.factorial(len(num_set))

num_set = set(list(range(1,N+1)))
ANS = [0 for i in range(N)]
for i in range(N):
    ANS[i] = sorted(list(num_set))[int(K / math.factorial(len(num_set)-1))]
    num_set.remove(ANS[i])
    K -= (ANS[i]-1) * math.factorial(len(num_set))

print(' '.join(map(str,ANS)))