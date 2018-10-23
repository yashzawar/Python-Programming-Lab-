import random
from random import randint as rt
out=0
faces=6
dice=3
for rolls in range(0,dice):
    out+=rt(1,faces)
print(out)