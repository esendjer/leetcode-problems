# Solved with Depth First Search (DFS)
# but I don't understand to the end
# what actually happens here
# It need to be re-learned more times until clear understanding
# 
# This problem also can and should be solved with 
# Breadth First Search (BFS)
class Solution:
    def isBipartite(self, graph) -> bool:
        self.graph = graph
        self.visited = [-1] * len(graph)
        color = 0
        res = True
        for i in range(len(graph)):
            if self.visited[i] == -1:
                res &= self.dfs(i, color)
        return res
    
    def dfs(self, index, color):
        if self.visited[index] == color:
            return False
        self.visited[index] = color
        ans = True
        for v in self.graph[index]:
            if self.visited[v] == -1:
                ans &= self.dfs(v, 1-color)
            if self.visited[v] == color:
                return False
        return ans


cases = (
    #  0       1      0              
    [[1,2,3],[0,2],[0,1,3],[0,2]],   # false
    [[1,3],[0,2],[1,3],[0,2]],       # true
    [[4,1],[0,2],[1,3],[2,4],[3,0]], # false
    [[1,4],[0,2],[1],[4],[0,3]],     # true
    [[3],[7,9],[],[0,5],[],[3],[9],[1],[],[1,6]], # true
    [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]], # false
)


a = Solution()
b = a.isBipartite
for i in cases:
    print(b(i))