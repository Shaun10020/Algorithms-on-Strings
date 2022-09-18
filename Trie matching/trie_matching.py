# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4

def build_trie(patterns):
    tree = dict()
    tree[0]={}
    for pattern in patterns:
        current_node=tree[0]
        for i in range(len(pattern)):
            symbol=pattern[i]
            if symbol in current_node:
                current_node=tree[current_node[symbol]]
            else:
                tree[len(tree)]={}
                current_node[symbol]=len(tree)-1
                current_node=tree[len(tree)-1]
    return tree

def solve (text, n, patterns):
	result = []

	tree=build_trie(patterns)
	for i in range(len(text)):
		current_text=text[i]
		current_node=tree[0]
		label=True
		j=0
		while label:
			if current_text in current_node:
				j+=1
				current_node=tree[current_node[current_text]]
				if not current_node:
					break
				if i+j>=len(text):
					label=False
					break
				current_text=text[i+j]
			else:
				label=False
		if label:
			result.append(i)
	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]
# n=1
# text='AATCGGGTTCAATCGGGGT'
# patterns=['ATCG','GGGT']

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
