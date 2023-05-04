class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = self.buildHeap(stones)
        while len(heap)>1:
            #remove the first heavy
            heap[0],heap[-1] = heap[-1],heap[0]
            y = heap.pop()
            heap = self.heapifyDown(heap,0)
            
            #remove the second heavy
            heap[0],heap[-1] = heap[-1],heap[0]
            x = heap.pop()
            heap = self.heapifyDown(heap,0)
        
            if x!=y:
                heap.append(y-x)
                self.heapifyUp(heap,len(heap)-1)

                
        if heap:
            return heap[0]
        
        else:
            return 0

    
    def buildHeap(self,arr):
        for i in range(len(arr)-1,-1,-1):
            arr = self.heapifyDown(arr,i)
            
        return arr
    
    def heapifyDown(self,arr,current):
        n = len(arr)
        while True:
            left = (current*2+1)
            right = (current*2+2)
            
            if left<n or right<n:
                if (left<n and right<n and arr[left]>arr[right]) or (left<n and right>=n):
                    if arr[left]>arr[current]:
                        arr[left],arr[current] = arr[current],arr[left]
                        current = left

                    else:
                        return arr
                    
                elif (left<n and right<n and arr[left]<=arr[right]) or (right<n and left>=n):
                    if arr[right]>arr[current]:
                        arr[right],arr[current] = arr[current],arr[right]
                        current = right
                        
                    else:
                        return arr
                    
                else:
                    return arr
                    
            else:
                return arr
            
    def heapifyUp(self,arr,current):
        parent = (current-1)//2
        
        while parent>=0 and arr[parent]<arr[current]:
            arr[current],arr[parent] = arr[parent],arr[current]
            current = parent
            parent = (current-1)//2
            
        return arr
