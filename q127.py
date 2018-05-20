class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordset = set()
        for word in wordList:
            wordset.add(word)
        
        # bfs
        queue = collections.deque([(beginWord,1)])
        if beginWord in wordset:
            wordset.remove(beginWord)
        
        visited = {}
        
        while queue:
            front = queue.popleft()
            curword = front[0]
            curstep = front[1]
            
            visited.clear() 
            for word in wordset:
                if self.similar(word, curword):
                    if word == endWord:
                        return curstep + 1
                    queue.append((word,curstep+1))
                    visited.add(word)
            for word in visited:
                wordset.remove(word)
        return 0
        
    def similar(self,word1,word2):
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
                if diff > 1:
                    return False
        return True
        
        
        
from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
            
        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i+1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0
        
        d = construct_dict(set(wordList) | set([beginWord]))
        return bfs_words(beginWord,endWord,d)
        
        
        
            
        