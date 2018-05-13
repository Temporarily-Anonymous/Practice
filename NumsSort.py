class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class NumsSort():
    def Counting_sorting(self, array):
        k = max(array)
        c = [0 for i in range(k + 1)]
        b = []
        for i in array:
            c[i] += 1
        for i in range(len(c)):
            for j in range(c[i]):
                b.append(i)
        print(b)

    def Cardinality_sorting(self, array):
        temp = []
        for i in range(3):
            for position in range(10):
                for num in array:
                    standard = int(num / pow(10, i)) % 10
                    if standard == position:
                        temp.append(num)
            array = temp
            temp = []
        print(array)

    def Bucket_sorting(self, array):
        zero = ListNode(0)
        one = ListNode(1)
        two = ListNode(2)
        three = ListNode(3)
        four = ListNode(4)
        five = ListNode(5)
        six = ListNode(6)
        seven = ListNode(7)
        eight = ListNode(8)
        nine = ListNode(9)
        bucket = [zero, one, two, three, four, five, six, seven, eight, nine]
        for i in range(3):
            for num in array:
                standard = int(num / pow(10, i)) % 10
                position = bucket[standard]
                while position.next is not None:
                    position = position.next
                position.next = ListNode(num)
            array = []
            for j in range(10):
                position = bucket[j]
                while position.next:
                    position = position.next
                    array.append(position.val)
            for j in range(10):
                bucket[j].next = None
            print(array)

Demo = NumsSort()
Demo.Bucket_sorting([329,457,657,839,436,720,355])
