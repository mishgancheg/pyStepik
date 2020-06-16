# N, M, K, A, B, C, D, X = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(
#     input()), int(input())
N, M, K, A, B, C, D, X = 7, 5, 11, 10, 12, 12, 2, 25
# N, M, K, A, B, C, D, X = 10, 11, 15, 18, 21, 20, 2, 25

NM = N + M - A - D
MK = M + K - B - D
KN = K + N - C - D

print(NM)
print(MK)
print(KN)

no_one = X - (N + M + K) + (NM + MK + KN) - D
exact_two = (NM + MK + KN) - 3 * D
exact_one = N + M + K - (NM + MK + KN) + 3 * D

print(exact_one)
print(exact_two)
print(no_one)
