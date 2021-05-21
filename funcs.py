def swap(a, b):
  return b,a

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def div():
    print("\n", "-" * 30, "\n")

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def partition(A, p, r):
  pivot = A[r]
  smaller = p
  for i in range(p, r):
    if A[i] <= pivot:
      A[i], A[smaller] = swap(A[i], A[smaller])
      smaller += 1
  A[r], A[smaller] = swap(A[r], A[smaller])
  return smaller

def quickSort(A, p, r):
  if(p < r):
    q = partition(A, p, r)
    quickSort(A, p, q-1)
    quickSort(A, q+1, r)
  return A

def heapify(A, size, i):
  largest = i
  l = left(i)
  r = right(i)

  if l < size and A[l] > A[i]:
      largest = l
  if r < size and A[r] > A[largest]:
      largest = r
  if i != largest:
      A[largest], A[i] = A[i], A[largest]
      return heapify(A, size, largest)
  else:
      return A

def heapBuild(A, size):
    for i in range(size // 2, -1, -1):
        A = heapify(A, size, i)
    return A

def heapSort(A, size):
    A = heapBuild(A, size)
    for i in range(size - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        A = heapify(A, i, 0)
    return A

def main():
    examples = [
        [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0],
        [84, 22, 19, 10, 3, 17, 6, 5, 9],
        [16, 4, 10, 14, 7, 9, 3, 2, 8, 1],
        [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    ]
    for example in examples:
        size = len(example)
        print("start:", example)

        result = heapBuild(example, size)
        print("build:", result)

        result = heapSort(example, size)
        print("heapsort:", result)
        div()