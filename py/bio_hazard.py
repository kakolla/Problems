


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

    # map for all poison pairs
    pairs = set()
    for i in range(m):
        p = (vulnerable_bacteria[i], toxic_bacteria[i])
        p2 = (toxic_bacteria[i], vulnerable_bacteria[i])
        pairs.add(p)
        pairs.add(p2)
    
    valid_pairs = 0

    # allocate all n samples
    samples = [i for i in range(1, n+1)] # 1 2 3
    l,r = 0, 0 # start with 1 elem
    while r < n: # stop condition (window at the end)
        # check if new plant will cause a poison pair
        subset = samples[l:r]
        poison = False
        for plant in subset:
            if (plant, samples[r]) in pairs:
                poison = True
                break
        
        while poison:
            l += 1
            subset = samples[l:r]
            poison = False
            for plant in subset:
                if (plant, samples[r]) in pairs:
                    poison = True
                    break
        # at this point, window has no poison pairs, from r:l, so every subwindow also is valid k:l
        valid_pairs += (r-l+1)
        
        r+= 1
        
    
    return valid_pairs

