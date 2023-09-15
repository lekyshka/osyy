import random
import argparse

parser = argparse.ArgumentParser(description='yeah')
parser.add_argument('-t')
args = parser.parse_args()
a = int(args.t)
arr = []
for i in range(a):
    arr.append(random.random())

for i in range(a-1):
    for j in range(a-1-i):
        if arr[j] > arr[j+1]:
            b = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = b
print(arr)