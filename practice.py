from collections import deque

MAX = float("inf")

class GoldenGate_Bridge():
    def __init__(self):
        self.group = {}
        self.costs = {}
        self.parents = {}
        self.processed = []
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

    def Create_Costs(self):
        for node in self.group:
            self.costs[node] = MAX
        self.costs[self.start] = 0

    def find_lowest_cost_node(self):
        lowest_cost = MAX
        lowest_cost_node = None
        for node in self.costs :
            cost = self.costs[node]
            if cost < lowest_cost and node not in self.processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def Traverse_Group(self):
        node = self.find_lowest_cost_node()
        while node is not None:
            cost = self.costs[node]
            neighbors = self.group[node]
            for n in neighbors:
                new_cost = cost + neighbors[n]
                if new_cost < self.costs[n]:
                    self.costs[n] = new_cost
                    self.parents[n] = node
            self.processed.append(node)
            node = self.find_lowest_cost_node()

    def Print_Data(self):
        # print (self.group)
        print (self.costs)
        print (self.parents)


Demo = GoldenGate_Bridge()
Demo.Create_Group()
Demo.Create_Costs()
Demo.Traverse_Group()
Demo.Print_Data()