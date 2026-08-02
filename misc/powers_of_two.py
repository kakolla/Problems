










# def check_power_two(num: int) -> bool:
#     return num > 0 and num & (num -1) == 0
#

def check_within(num, index, m):
    # check if num + another one can equal power of two
    
    total = 0

    max_sum = 2 * (1000000)
    c = 1
    # a + b = power of 2

    while c <= max_sum:
        if c - num in m and index <= m[c-num]:
            total += 1
        c *= 2

    return total

       

def lookup_table(numbers: list[int] ) -> int:
    # number of i,j (i<=j), num[i] + num[j] = power of 2
    m = {}
    for i, n in enumerate(numbers):
        m[n] = i # index of this number

    ans = 0
    for i in range(len(numbers)):
        ans += check_within(numbers[i], i, m)

    return ans




TESTS = [
    ([1, -1, 2, 3], 5),          # self: 1+1, 2+2 | cross: 1+3, -1+2, -1+3
    ([3, 1, -1, 2], 5),          # order shouldn't matter
    ([1], 1),                    # i == j counts
    ([3], 0),
    ([0], 0),                    # 0+0=0 is NOT a power of 2
    ([-5, 5], 0),                # sum 0 — catches the & bug
    ([-4, -1], 0),               # negative sums
    ([5, 7], 0),
    ([-5, 6], 1),                # sum 1 = 2**0
    ([-3, 4], 2),                # sum 1, plus 4+4=8
    ([0, 1, 2], 4),              # 1+1, 2+2, 0+1, 0+2
    ([1, 2, 4, 8, 16], 5),       # all from i == j, zero cross pairs
    ([1, 3, 5, 7, 9, 11, 13, 15], 8),
    ([1000000, 48576], 1),       # 2**20, largest reachable sum
    ([-1000000, 1000000], 0),
    ([-999999, 1000000], 1),
]

for arr, want in TESTS:
    got = lookup_table(list(arr))
    print("ok " if got == want else "FAIL", arr, "-> got", got, "want", want)








import random
POW = {1 << k for k in range(22)}

def brute(a):
    return sum(a[i] + a[j] in POW for i in range(len(a)) for j in range(i, len(a)))

for seed in range(300):
    r = random.Random(seed)
    arr = r.sample(range(-40, 41), r.randint(1, 12))
    if lookup_table(list(arr)) != brute(arr):
        print("FAIL", arr, lookup_table(list(arr)), brute(arr))
        break
else:
    print("random ok")


import time
big = list(range(-50_000, 50_000))
t = time.perf_counter(); lookup_table(big); print(f"{time.perf_counter()-t:.2f}s")
