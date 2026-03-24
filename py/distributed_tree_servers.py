





from collections import deque
def bfs(start, adj, num_tree_nodes):
    # do a bfs and get the shortest distances
    dists = [-1] * (num_tree_nodes+1)
    dists[start] = 0 # init start node
    q = deque()
    q.append((start))

    while q:
        f = q.popleft()
        for nei in adj[f]:
            if dists[nei] == -1:
                dists[nei] = dists[f] + 1
                q.append(nei)
    return dists 



from itertools import permutations
def getMinimumTime(tree_nodes: int, tree_from: list[int], tree_to: list[int], start_node: int, end_node: int, num_tasks, task_nodes: list[int]):

    # start at start_node, 
    # must complete tasks (visit task_nodes)
    # end at end node

    # create adj list
    adj = [[] for i in range(tree_nodes+1)] # 1 2 .. treenodes
    for i in range(len(tree_from)):
        adj[tree_from[i]].append(tree_to[i]) 
        adj[tree_to[i]].append(tree_from[i]) 

    # run a bfs to get shortest path for every start position
    # shorest from [a, b]
    all_key_nodes = [start_node, end_node] + task_nodes
    distances = {}
    for keynode in all_key_nodes:
        distances[keynode] = bfs(keynode, adj, tree_nodes)

    mindist = float('inf')
    perms = permutations(task_nodes)
    # check every possible path, pick min
    for perm in perms:
        time_to = distances[start_node][perm[0]] # start to first task

        for i in range(len(perm)-1):
            # task to task
            time_to += distances[perm[i]][perm[i+1]]
        time_to += distances[perm[len(perm)-1]][end_node]   
        mindist = min(mindist, time_to)
        
    print(distances)
    return mindist


    




    
print(getMinimumTime(4, [1,2,2], [3,3,4], 1, 2, 1, [4]))












    


























