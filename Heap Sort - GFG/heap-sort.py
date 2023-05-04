# User function Template for python3

class Solution:
    # Heapify function to maintain heap property.
    def heapifyDown(self, arr, n, i):
        current = i

        while True:
            left = (2*current+1)
            right = (2*current+2)

            if left >= n:
                left = None

            if right >= n:
                right = None

            if left and right:
                if arr[left] < arr[right]:
                    if arr[left] < arr[current]:
                        arr[left], arr[current] = arr[current], arr[left]
                        current = left

                    else:
                        return arr

                else:
                    if arr[right] < arr[current]:
                        arr[right], arr[current] = arr[current], arr[right]
                        current = right

                    else:
                        return arr

            elif right:
                if arr[right] < arr[current]:
                    arr[right], arr[current] = arr[current], arr[right]
                    current = right

                else:
                    return arr

            elif left:
                if arr[left] < arr[current]:
                    arr[left], arr[current] = arr[current], arr[left]
                    current = left

                else:
                    return arr

            else:
                return arr

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        heap = arr.copy()
        for ind in range(n-1, -1, -1):
            heap = self.heapifyDown(heap, n, ind)

        return heap

    # Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        tmpArr = arr.copy()

        heap = self.buildHeap(tmpArr, n)
        i = 0

        while heap:
            heap[0], heap[-1] = heap[-1], heap[0]
            arr[i] = heap.pop()
            heap = self.heapifyDown(heap, len(heap), 0)
            i += 1
            
        return arr
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends