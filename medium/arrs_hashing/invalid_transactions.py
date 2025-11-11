"""
# create a map of list of transactions under a name
    # sort transactions under each name
    # check if transaction is within 60 mins (while loop 2 ptrs) - this is O(n^2)
        # tally invalids
    # also check if > $1000

    in each transaction, also add on the string version so we don't have to reconstruct

"""
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # i:
        # "name, time, amount, city"

        # create a map of list of transactions under a name
        # sort transactions under each name
        # check if transaction is within 60 mins (while loop 2 ptrs)
            # tally invalids
        # also check if > $1000

        invalids = set() # so we don't have dupes
        trans = [] # tuple (name, time, amount, city)

        from collections import defaultdict
        names_map = defaultdict(list)
        for t in transactions:
            name, time, amt, city = t.split(",")
            # also keep track of og string at end
            names_map[name].append([name, int(time), int(amt), city, t])

        for name in names_map:
            # sort based on times
            names_map[name].sort(key=lambda x: x[1])
        
        # for each transaction
        for name in names_map:
            items = names_map[name]
            # make sure window time[j] - time[i] <= 60
            i = 0
            while i < len(items):
                if items[i][2] > 1000:
                    invalids.add(items[i][4]) # add og string
                j = i + 1
                while j < len(items) and items[j][1] - items[i][1] <= 60:
                    if items[j][3] != items[i][3]:
                        # diff city
                        invalids.add(items[i][4])
                        invalids.add(items[j][4])
                    j += 1 # incr window if <= 60
                i += 1 # decr i if window > 60 (time)
     
        # make sure even transactions that are equal but distinct are tracked
        return [t for t in transactions if t in invalids]