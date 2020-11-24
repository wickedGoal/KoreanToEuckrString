import sys

def convString(kor):
    return kor.encode("euc-kr").encode("utf-8","backslashreplace")

if __name__ == '__main__':
    print(convString(sys.argv[1]))
