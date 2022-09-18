#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
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


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    # patterns=['ATA']
    # patterns=['AT','AG','AC']
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
