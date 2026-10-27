class Solution:
    def createGrid(self, m, n):
        d = min(m, n) - 1  
        gate = (d, 0) if m <= n else (0, d)  
        return ["".join(".#"[i + j == d and (i, j) != gate] for j in range(n)) for i in range(m)]