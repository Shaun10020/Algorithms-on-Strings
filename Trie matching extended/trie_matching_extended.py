# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4
		self.patternEnd = False

class Trie:
	def __init__(self):
		self.root=self.getNode()

	def getNode(self):
		return Node()

	def ToIndex(self,cha):
		if cha=='A':
			return 0
		elif cha =='C':
			return 1
		elif cha=='T':
			return 2
		elif cha =='G':
			return 3

	def insert(self,key):
		node=self.root
		for character in range(len(key)):
			index = self.ToIndex(key[character])
			if node.next[index] ==-1:
				node.next[index] = self.getNode()
			node = node.next[index]
		node.patternEnd = True

	def pattern_matching(self,string):
		result=[]
		for character in range(len(string)):
			node=self.root
			index = self.ToIndex(string[character])
			j=0
			while node.next[index]!=-1:
				node=node.next[index]
				if node.patternEnd:
					result.append(character)
					break
				j+=1
				if character+j>=len(string):
					break
				index=self.ToIndex(string[character+j])
		return result

def solve (text, n, patterns):
	t= Trie()
	for pattern in patterns:
		t.insert(pattern)
	result=t.pattern_matching(text)
	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]
# n=1
# text='ACATA'
# patterns=['A','AG','AT']

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
