'''
이항계수 공식
nCk = n!/(n-k)!k!
사칙연산 순서 틀려서 틀림... 하...
'''

def facto(n):
    if n <= 1:
        return 1
    return n * facto(n-1)

N, K = map(int, input().split())
result = facto(N) // (facto(N-K) * facto(K))
print(result)