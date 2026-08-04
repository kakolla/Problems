












def solution(operations):

    ans = []


    from collections import defaultdict
    accounts = defaultdict(lambda: 0)


    # pending = defaultdict(list)
    pending_ids = set()
    transfers_map = {}
    id = 1
    for i in range(len(operations)):
        kind = operations[i][0]
        if kind == 'create':
            accid = operations[i][1]
            if accid not in accounts:
                # success
                accounts[accid] = 0
                ans.append(True)
            else:
                # fail
                ans.append(False)
        elif kind == 'deposit':
            accid = operations[i][1]
            if accid not in accounts:
                #fail
                ans.append(None)
            else:
                amount = operations[i][2]
                # success, return balance
                accounts[accid] += amount # amount
                ans.append(accounts[accid])
        elif kind == 'transfer':
            # rejected
            src, dest, amount, timestamp = operations[i][1:]
            if src == dest or src not in accounts or dest not in accounts or accounts[src] < amount:
                ans.append(None)
            else:
                accounts[src] -= amount
                ans.append(id)
                pending_ids.add(id)
                transfers_map[id] = (src, dest, amount)
                id += 1

        elif kind == 'accept':
            dst, transfer_id, timestamp = operations[i][1:]
            found = -1
            if transfer_id not in pending_ids:
                ans.append(False)
                continue
            if transfers_map[transfer_id][1] != dst or dst not in accounts:
                ans.append(False)
                continue
            # good
            accounts[dst] += transfers_map[transfer_id][2]
            pending_ids.remove(transfer_id)
            transfers_map.pop(transfer_id)
            ans.append(True)
        elif kind == 'balance':
            accid, timestamp = operations[i][1:]
            if accid in accounts:
                ans.append(accounts[accid])
            else:
                ans.append(None)





                   

                
    return ans

        
    












    pass











