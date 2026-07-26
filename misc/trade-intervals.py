







"""

exposure = holding the stock

: [tradeId, time, "buy" or "sell"]


track whether we are exposed are not

"""


def getExposureIntervals(events):
    # TODO: return merged list of [start, end] intervals where exposure > 0
    # [[tradeid, time, 'buy/sell']]
    # 10^5 events

    """
    1, 8
    3 12
    -> 1 12

    1, 5
    7, 12
    -> (1,5). (7,12)



    | ---- |
        | ----- |

    | --- | | --- |

    | ---||---|

    | ----|
       |-|

    """
    sorted_events = sorted(events, key= lambda x: x[1])
    intervals = [] # we hold at least one stock

    # process: put all orders under a start, end
    from collections import defaultdict
    trademap = defaultdict(lambda: [0,0])

    for tradeid, time, side in events:
        if side == "buy":
            trademap[tradeid][0] = time
        elif side == "sell":
            trademap[tradeid][1] = time

    # build events
    new_events = []
    for tradeid,metadata in trademap.items():
        new_events.append([metadata[0], metadata[1]]) # buy, sell times - time they are 'open'




    print("88")
    print(new_events)
    print("88")

    new_events = sorted(new_events, key= lambda x: x[0]) # sort by start time
    for time, end in new_events:
        if len(intervals) == 0:
            intervals.append([time, end])
        else:
            top_end = intervals[-1][1]
            if top_end > end:
                continue
            elif top_end >= time:
                # merge
                top_start = intervals[-1][0]
                intervals.pop()
                intervals.append([top_start, end])
                pass
            elif top_end < time:
                # add on 
                intervals.append([time, end])
    
    return intervals




tests = [
    # single trade, no overlap
    ([[1, 1, "buy"], [1, 5, "sell"]],
     [[1, 5]]),

    # two disjoint trades, no overlap
    ([[1, 1, "buy"], [1, 3, "sell"], [2, 5, "buy"], [2, 8, "sell"]],
     [[1, 3], [5, 8]]),

    # two overlapping trades -> merged into one interval
    ([[1, 1, "buy"], [1, 6, "sell"], [2, 3, "buy"], [2, 9, "sell"]],
     [[1, 9]]),

    # unsorted input
    ([[2, 5, "buy"], [1, 1, "buy"], [1, 3, "sell"], [2, 8, "sell"]],
     [[1, 3], [5, 8]]),

    # back-to-back (sell time == next buy time) -- ambiguous, clarify with interviewer
    ([[1, 1, "buy"], [1, 5, "sell"], [2, 5, "buy"], [2, 9, "sell"]],
     [[1, 9]]),  # assumes touching intervals merge

    # three overlapping trades, nested
    ([[1, 1, "buy"], [1, 10, "sell"], [2, 2, "buy"], [2, 4, "sell"], [3, 5, "buy"], [3, 6, "sell"]],
     [[1, 10]]),
]

for events, expected in tests:
    result = getExposureIntervals(events)
    status = "PASS" if result == expected else "FAIL"
    print(f"{events}")
    print(f"  got {result}, expected {expected}  [{status}]")
