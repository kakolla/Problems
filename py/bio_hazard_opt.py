


def experiment(n: int, m: int, vulnerable_bacteria: list[int], toxic_bacteria: list[int]) -> int:
    """
    n = 3, 
    m = 1, 
    vulnerable_bacteria = [1], 
    toxic_bacteria = [2] 
    Output: 4 
    """

    """
    interval is: i,j for samples[i:j)
    goal: we dont want any poisonous pair in the interval
    sliding window
    """
    plants = [i for i in range(1, n+1)]

    # lets map poison pairs
    from collections import defaultdict
    pairs = defaultdict(list)
    for i in range(m):
        pairs[vulnerable_bacteria[i]].append(toxic_bacteria[i])
        pairs[toxic_bacteria[i]].append(vulnerable_bacteria[i])

    # sliding win approach
    l,r = 0, 0
    last_seen = {}

    ans =0

    while r < n:
        curr = plants[r] # entering window

        # check if it causes poison (see if in the last seen map, there is a poison pair we know)
        for poisonous_other in pairs[curr]:
            if poisonous_other in last_seen and last_seen[poisonous_other] >= l:
                # it is in the window, skip over it 
                # 1 2 P 3 4 _, skip to P+1
                l = last_seen[curr] + 1

        ans += (r-l+1) # this many subwindows are valid
        last_seen[curr] = r
        r += 1

    return ans


