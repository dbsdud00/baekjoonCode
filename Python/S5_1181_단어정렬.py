# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오
#   1. 길이가 짧은 것 부터
#   2. 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.
import sys
N = int(sys.stdin.readline()) # 단어의 갯수 N개
A = [sys.stdin.readline().strip() for i in range(N)]    # 단어 N개를 입력받아서 A 리스트에 저장
X = list(set(A)) # set() 함수를 통해 중복을 제거하고 다시 리스트에 넣어서 X에 저장한다
X.sort(key= lambda x: (len(x), x) )     # X를 sort함수를 통해 정렬하는데 key값을 lambda를 통해 다중조건을 건다.
                                        #   len(x)로 먼저 길이가 짧은 순으로 정렬 후 x를 통해 사전순으로 정렬된다.
for j in X:     # 출력한다.
    print(j)