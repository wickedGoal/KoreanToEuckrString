import sys

def convString(kor):
    return kor.encode("euc-kr").decode("utf-8","backslashreplace").replace("x","'")

if __name__ == '__main__':
    print(convString(sys.argv[1]))
