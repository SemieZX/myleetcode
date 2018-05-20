from collections import deque

class Solution(object):
	def ladderLenth(self,beginword,endword,wordlist):
		def construct_dict(word_list):
			d = {}
			for word in word_list:
				for i in range(len(word)):
					s = word[:i] + "_" + word[i+1:]
					# the value is a list
					d[s] = d.get(s,[]) + [word]
			return d
	def bfs_words(begin,end,dict_words):
		queue, visited = deque([(begin,1)]), set()
		while queue:
			word,steps = queue.popleft()
			if word not in visited:
				visited.add(word)
				if word == end:
					return steps
				for i in range(len(words)):
					s = word[:i] + "_" + words[i+1:]
					neigh_words = dict_words.get(s,[])
					# return the value of dict eg:d[s]
					for neigh in neigh_words:
						if neigh not in visited:
							queue.append((neigh,steps+1))
		return 0

	d = construct_dict(set(word_list)|set([beginword]))
	return bfs_words(beginword,endword,d)
