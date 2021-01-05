"""
    692. Top K Frequent Words
    Given a non-empty list of words, return the k most frequent elements.
    Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
"""
from collections import Counter, OrderedDict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        countDict = Counter(words)

        countDict = OrderedDict(sorted(countDict.items(), 
                                       key=lambda kv: kv[1], 
                                       reverse=True))
        ordered_list = list()
        for i in sorted(set(countDict.values()), reverse=True):
            ordered_list += sorted([k for k,v in countDict.items() if v == i])
        
        return ordered_list[:k]