S=str(input())

import string
alphabet="".join([i for i in string.ascii_lowercase if i not in S])

if(alphabet):
  print(alphabet[0])
else:
  print("None")
