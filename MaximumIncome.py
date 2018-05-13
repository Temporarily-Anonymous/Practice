global MAX
MAX = 0
global Left
global Right
def MaximumSubarray(array, start):
    global MAX
    global Left
    global Right
    if len(array) == 1:
        return array[0]
    mid = int(len(array)/2)
    mid_left = 0
    mid_right = 0
    left = start + mid
    right = start + mid
    temp = 0
    for i in range(mid - 1, -1, -1):
        temp += array[i]
        if temp > mid_left:
            mid_left = temp
            left = start + i
    temp = 0
    for i in range(mid,len(array)):
        temp += array[i]
        if temp > mid_right:
            mid_right = temp
            right = start + i
    mid_max = mid_left + mid_right
    if mid_max > MAX:
        MAX = mid_max
        Left = left
        Right = right
    return max(mid_max,MaximumSubarray(array[:mid], start),MaximumSubarray(array[mid:], start + mid))

array = [13,-3,-25,20,-3,-5,-22,15,-4,7,-16,-23,18,20,-7,12]
result = MaximumSubarray(array, 0)
print(result)
print(Left,Right)