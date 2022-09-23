class pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
 
# Returns adjacency list representation from a list
# of pairs.
def make_graph(numTasks, prerequisites):
    graph = []
    for i in range(numTasks):
        graph.append([])
 
    for pre in prerequisites:
        graph[pre.second].append(pre.first)
 
    return graph
 
# A DFS based function to check if there is a cycle
# in the directed graph.
def dfs_cycle(graph, node, onpath, visited):
    if visited[node]:
        return false
    onpath[node] = visited[node] = True
    for neigh in graph[node]:
        if (onpath[neigh] or dfs_cycle(graph, neigh, onpath, visited)):
            return true
    return False
 
# Main function to check whether possible to finish all
# tasks or not
def canFinish(numTasks, prerequisites):
    graph = make_graph(numTasks, prerequisites)
    onpath = [False]*numTasks
    visited = [False]*numTasks
    for i in range(numTasks):
        if (not visited[i] and dfs_cycle(graph, i, onpath, visited)):
            return False
    return True
