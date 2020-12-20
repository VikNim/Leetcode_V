class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        i1, i2, dist = None, None, len(words)
        for i, j in enumerate(words):
            print(i, j)
            if j == word1:
                i1 = i
            elif j == word2:
                i2 = i
            temp_dist = abs(i1-i2) if i1 is not None and i2 is not None else len(words) 
            dist = temp_dist if temp_dist < dist else dist
        return dist