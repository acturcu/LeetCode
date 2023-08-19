class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sums = []
        for ind, row in enumerate(mat):
            sums.append([sum(row), ind])
        sums.sort()
        index = []
        for el in sums:
            index.append(el[1])
        
        return index[0:k]
