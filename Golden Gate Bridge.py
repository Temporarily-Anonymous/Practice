from collections import deque

MAX = 100

class GoldenGate_Bridge():
    def __init__(self):
        self.group = {}
        self.queue = deque()
        self.distance_list = {}
        self.start = "双子峰"

    def Create_Group(self):
        self.group["双子峰"] = {}
        self.group["双子峰"]["左上"] = 4
        self.group["双子峰"]["左下"] = 1
        self.group["左上"] = {}
        self.group["左上"]["右上"] = 21
        self.group["左下"] = {}
        self.group["左下"]["中"] = 5
        self.group["左下"]["右下"] = 8
        self.group["中"] = {}
        self.group["中"]["右上"] = 5
        self.group["右上"] = {}
        self.group["右上"]["金门大桥"] = 4
        self.group["右下"] = {}
        self.group["右下"]["右上"] = 12
        self.group["金门大桥"] = {}

    def Create_List(self):
        for location in self.group:
            self.distance_list[location] = MAX
        self.distance_list[self.start] = 0

    def Traverse_Group(self):
        self.father = {}
        for location in self.group[self.start]:
            self.queue += [[location, self.start]]
            self.father[location] = self.start
        while self.queue:
            location, last_location = self.queue.popleft()
            if self.distance_list[last_location] + self.group[last_location][location] < self.distance_list[location]:
                self.distance_list[location] = self.distance_list[last_location] + self.group[last_location][location]
                self.father[location] = last_location
            for next_location in self.group[location]:
                self.queue += [[next_location, location]]


    def Print_Data(self):
        print (self.group)
        print (self.distance_list)
        print (self.father)

# Demo = GoldenGate_Bridge()
# Demo.Create_Group()
# Demo.Create_List()
# Demo.Traverse_Group()
# Demo.Print_Data()