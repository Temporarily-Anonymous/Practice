class HeapSorting:
    def MaxHeapify(self, array, i):
        length = len(array)
        left = 2*(i+1) - 1
        right = left + 1
        largest = i
        if left < length and array[left] > array[i]:
                largest = left
        if right < length and array[right] > array[left] and array[right] > array[i]:
                largest = right
        if largest is not i:
            temp = array[i]
            array[i] = array[largest]
            array[largest] = temp
            self.MaxHeapify(array, largest)

    def BuildMaxHeap(self,array):
        length = len(array)
        for i in range(int(length/2) - 1, -1, -1):
            self.MaxHeapify(array,i)
        return array

    def Maxium(self, array):
        if len(array) < 1:
            return 0
        return array[0]

    def ExtractMax(self, array):
        length = len(array)
        if length < 1:
            return 0
        max = array[0]
        array[0] = array[length - 1]
        array = array[:length - 1]
        self.MaxHeapify(array, 0)
        return max, array

    def IncreaseKey(self, array, i, key):
        if key < array[i]:
            return 0
        array[i] = key
        while i > 0 and array[int((i+1)/2) - 1] < array[i]:
            temp = array[int((i + 1) / 2) - 1]
            array[int((i + 1) / 2) - 1] = array[i]
            array[i] = temp
            i = int((i+1)/2) - 1
        return array

    def Insert(self, array, key):
        length = len(array)
        array.append(float("-inf"))
        return self.IncreaseKey(array, length, key)



array = [4,1,3,2,16,9,10,14,8,7]
Demo = HeapSorting()
heap = Demo.BuildMaxHeap(array)
new_heap = Demo.Insert(heap, 15)
print(new_heap)