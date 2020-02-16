N=int(input())

A=[]
for i in range(N):
    A.append(input())

B=sorted(A)

import collections
import itertools

counter = collections.Counter(A)

mode_v = counter.most_common()[0][-1]
it = itertools.takewhile(lambda kv: kv[-1] == mode_v, counter.most_common())

answer=[]
for i in it:
    answer.append(i[0])

answer.sort()
for i in answer:
    print(i)
