# python3
import sys


def SortCharacters(S):
    order = [0]*len(S)
    count = {}
    elements = []
    set_char = set(S)
    for i in range(len(set(S))):
        element = set_char.pop()
        count[element] = 0
        elements.append(element)
    elements.sort(reverse=True)
    for i in range(len(S)):
        count[S[i]] += 1
    for j in range(len(set(S))):
        if j == 0:
            continue
        count[elements[j]] += count[elements[j-1]]
    for i in range(len(S)):
        i = len(S)-1-i
        c = S[i]
        count[c] -= 1
        order[count[c]] = i
    # print(list(reversed(order)))
    return list(reversed(order))


def ComputeCharClasses(S, order):
    classes = [0]*len(S)
    classes[order[0]] = 0
    for i in range(len(S)):
        if i == 0:
            continue
        if S[order[i]] != S[order[i-1]]:
            classes[order[i]] = classes[order[i-1]]+1
        else:
            classes[order[i]] = classes[order[i-1]]
    # print(classes)
    return classes


def SortDoubled(S, L, order, classes):
    count = [0]*len(S)
    neworder = [None]*len(S)
    for i in range(len(S)):
        count[classes[i]] += 1
    for j in range(len(S)):
        if j == 0:
            continue
        count[j] += count[j-1]
    for i in range(len(S)):
        i = len(S)-1-i
        start = (order[i]-L+len(S)) % len(S)
        cl = classes[start]
        count[cl] -= 1
        neworder[count[cl]] = start
    # print(neworder)
    return neworder


def UpdateClasses(newOrder, classes, L):
    n = len(newOrder)
    newclass = [None]*n
    newclass[newOrder[0]] = 0
    for i in range(n):
        if i == 0:
            continue
        cur = newOrder[i]
        prev = newOrder[i-1]
        mid = cur+L
        midPrev = (prev+L) % n
        if classes[cur] != classes[prev] or classes[mid] != classes[midPrev]:
            newclass[cur] = newclass[prev]+1
        else:
            newclass[cur] = newclass[prev]
    # print(newclass)
    return newclass


def build_suffix_array(text):
    order=SortCharacters(text)
    classes=ComputeCharClasses(text,order)
    L=1
    while L<len(text):
      order=SortDoubled(text,L,order,classes)
      classes=UpdateClasses(order,classes,L)
      L=2*L
    return order


if __name__ == '__main__':
    text = 'AACGATAGCGGTAGA$'
    print(" ".join(map(str, build_suffix_array(text))))
