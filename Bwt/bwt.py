# python3
import sys

def rotateright(text):
    first=text[len(text)-1]
    return first+text[0:len(text)-1]

def BWT(text):
    string=''
    array=[]
    for level in range(len(text)):
        text=rotateright(text)
        array.append([text,len(text)-level])
    array.sort()
    for length in range(len(array)):
        string+=array[length][0][len(text)-1]
    return string

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    # text='AGACATA$'
    print(BWT(text))