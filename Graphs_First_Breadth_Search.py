#REPRESENTING THE GRAPH:
"""
The graph shown is a directed graph because the outer nodes do not have an
arrow directed from them to the inner nodes.

Directed graph:
bob -----> anuj

Undirected graph:
bob -----> anuj
    <------
"""
graph = {}
graph["you"] = ["alice", "bob", "claire", "timber"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy", "nathan"]
graph["claire"] = ["thom_m", "jonny", "timber"]
graph["anuj"] = ["timber"]
graph["peggy"] = []
graph["thom_m"] = []
graph["jonny"] = ["nathan"]
graph["nathan"]=[]
graph["timber"] = []

from collections import deque

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    #print(f"Searching through {name}'s list of friends")

    while search_queue:
        
        person = search_queue.popleft()
        
        if not person in searched:
            print(person)
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
                
    return False


def person_is_seller(name):
    return name[-2:] == "gy"


def pathfinder(graph, root, target):
    if root == target:
        return[target]

    else:
        visited = []
        for new_root in graph[root]:
            print(f"new root: {new_root}")
            if new_root not in visited:
                visited.append(new_root)
                sub_path = pathfinder(graph, new_root, target)
                print(f"Subpath for {new_root} is {sub_path}")
                if sub_path is not None:
                    print(f"visited: {visited}")
                    return [root] + sub_path

"""
Pathfinder:

Takes in the root and destination or target. It also takes in the network or graph.

Base Case: It first checks whether the root and destination are the same

Recursion:
- Create a list that holds the visited nodes so we don't have to come back to them.
- Runs a loop over the nodes following the root node
- Each node visited is appended to the visited list.
- The pathfinder function is called again:
    - In the recursive call, the current node it is in, is compared with the target.
    - If it is not the target, we continue to the else.
    - In the else, another visited list is created.
    - Another loop is done over the nodes connected to the current node and the process
    continues.
- If the recursive call of the pathfinder function does not return a None value, then,
it means that we finally reached our base case and can thus return the path.
- If the recursive call of the pathfinder function returns a None value because
the base case could not be reached, then, that recursive call ends and then
goes back and branches into another path.
"""



##
##def shortest_path(graph, root, target):
##    possible_paths = [] 
##
##    if root == target:
##        return[target]
##
##    else:
##        visited = []
##        for new_root in graph[root]:
##            print(f"new root: {new_root}")
##            if new_root not in visited:
##                visited.append(new_root)
##                sub_path = shortest_path(graph, new_root, target)
##                print(f"Subpath for {new_root} is {sub_path}")
##                if sub_path is not None:
##                    print(f"visited: {visited}")
##                    possible_paths.append([root] + sub_path)
##        return possible_paths


def possible_paths(path_func, graph, source, target):
    discovered_paths = []
    for node in graph.keys():
        node_path = path_func(graph, node, target)
        if  node_path is not None:
            if set([node]).issubset(set(graph[source])) and source not in node_path:
                discovered_paths.append(["you"] + node_path)
    return discovered_paths


def shortest_path(graph, root, target):
    possible_paths = {}

    if root == target:
        return[target]

    else:
        visited = []
        for new_root in graph[root]:
            print(f"new root: {new_root}")
            if new_root not in visited:
                visited.append(new_root)
                
                sub_path = shortest_path(graph, new_root, target)
                print(f"Subpath for {new_root} is {sub_path}")
                if sub_path is not None:
                    print(f"visited: {visited}")
                    x = [root] + sub_path
                    possible_paths[new_root] = x
                    return possible_paths


def pathfinder2(graph, root, target):

    search_queue = deque()
    search_queue += graph[name]
    searched = []

    if root == target:
        return[target]

    else:
        visited = []
        for new_root in graph[root]:
            print(f"new root: {new_root}")
            if new_root not in visited:
                visited.append(new_root)
                sub_path = pathfinder(graph, new_root, target)
                print(f"Subpath for {new_root} is {sub_path}")
                if sub_path is not None:
                    print(f"visited: {visited}")
                    return [root] + sub_path
