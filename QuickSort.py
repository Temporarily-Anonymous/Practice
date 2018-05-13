class QuickSort:
    def Partition(self, array, left, right):
        standard = right
        right -= 1
        while left < right:
            if array[left] > array[standard] and array[right] < array[standard]:
                temp = array[left]
                array[left] = array[right]
                array[right] = temp
            if array[left] < array[standard]:
                left += 1
            if array[right] > array[standard]:
                right -= 1
        if array[left] < array[standard]:
            left += 1
        temp = array[left]
        array[left] = array[standard]
        array[standard] = temp
        return left

    def QuickSort(self, array, left, right):
        if left < right:
            middle = self.Partition(array, left, right)
            self.QuickSort(array, left, middle - 1)
            self.QuickSort(array, middle + 1, right)

array = [4,1,3,2,16,9,10,14,8,7,11,5,33,42,19,21,55,44,32,29,28,22,25]
Demo = QuickSort()
Demo.QuickSort(array, 0, len(array) - 1)
print(array)