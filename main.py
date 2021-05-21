from funcs import *
import cProfile, random
import sys

sys.setrecursionlimit(10000)
print("Recursion limit set: ", sys.getrecursionlimit())

length = 5000
sortedArr = [i for i in range(length)]
reversedArr = [i for i in range(length, -1, -1)]
randomArr = [random.randint(0, length) for i in range(length)]

for example in [sortedArr, reversedArr, randomArr]:
  size = len(example) - 1
  for sortMethod in ["quickSort(example, 0, size)", "heapSort(example, size)", "bubbleSort(example)"]:
    div()
    print(sortMethod, namestr(example, globals())[0])
    cProfile.run(sortMethod)
    div()