N = input()

if '0' not in N:
    print(-1)
else:
    N = [int(n) for n in N]
    if sum(N) % 3 == 0:
        N = sorted(N, reverse=True)
        N = [str(n) for n in N]
        N = ''.join(N)
        print(N)
    else:
        print(-1)