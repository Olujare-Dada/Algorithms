from collections import deque




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



class FirstBreadthSearch:

    discovered_paths = []
    #discovered_paths.clear()


    def __init__(self, graph):
        self.graph = graph
        self.discovered_paths = []
        
        return
    
    def search(self, name, attribute):
        search_queue = deque()
        search_queue += self.graph[name]
        searched = []
        #print(f"Searching through {name}'s list of friends")

        while search_queue:
            
            person = search_queue.popleft()
            
            if not person in searched:
                print(person)
                if self._person_is_seller(person, attribute):
                    print(person + " is a mango seller!")
                    return True
                else:
                    search_queue += self.graph[person]
                    searched.append(person)
                    
        return False


    def _person_is_seller(self, name, attribute):
        return name[-2:] == attribute


    def pathfinder(self, graph, root, target):
        if root == target:
            return[target]

        else:
            visited = []
            for new_root in graph[root]:
                print(f"new root: {new_root}")
                if new_root not in visited:
                    visited.append(new_root)
                    sub_path = self.pathfinder(graph, new_root, target)
                    print(f"Subpath for {new_root} is {sub_path}")
                    if sub_path is not None:
                        print(f"visited: {visited}")
                        return [root] + sub_path



    def possible_paths(self, graph, source, target):
##        self.discovered_paths = []FirstBreadthSearch.discovered_paths.copy()
##        print(self.discovered_paths)
        self.discovered_paths.clear()
        FirstBreadthSearch.discovered_paths.clear()
        for node in graph.keys():
            node_path = self.pathfinder(graph, node, target)
            if  node_path is not None:
                if set([node]).issubset(set(graph[source])) and source not in node_path:
                    self.discovered_paths.append(["you"] + node_path)
        print(self.discovered_paths)
        FirstBreadthSearch.discovered_paths  = self.discovered_paths.copy()
        print(FirstBreadthSearch.discovered_paths)
        return type(self)(self.discovered_paths)
        #return self.discovered_paths



    def shortest_path(self):
        self.discovered_paths = FirstBreadthSearch.discovered_paths.copy()
        FirstBreadthSearch.discovered_paths.clear()
        path_indices = [len(path) for path in self.discovered_paths]
        print(path_indices)
        shortest_path_index = path_indices.index(min(path_indices))
        return self.discovered_paths[shortest_path_index]
            
