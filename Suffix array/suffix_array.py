# python3
import sys


def rotateright(text):
    first = text[len(text)-1]
    return first+text[0:len(text)-1]


def build_suffix_array(text):
    array = []
    result=[]
    for level in range(len(text)):
        text = rotateright(text)
        array.append([text, len(text)-level-1])
    array.sort()
    for length in range(len(array)):
        result.append(array[length][1])
    return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  # text='AACGATAGCGGTAGA$'
  print(" ".join(map(str, build_suffix_array(text))))
