class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result = 0
        n = len(grid)
        mappings = defaultdict(int)
        for i in range(n):
            mappings[tuple(grid[i])] += 1
        for j in range(n):
            col = []
            for k in range(n):
                col.append(grid[k][j])
            if tuple(col) in mappings:
                result += mappings.get(tuple(col))
        return result