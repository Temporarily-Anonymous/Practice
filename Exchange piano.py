from collections import deque

MAX = 1000

class Exchange_piano():
    def __init__(self):
        self.group = {}
        self.price = {}
        self.start = "乐谱"
        self.queue = deque()

    def create_group(self):
        self.group["乐谱"] = {}
        self.group["乐谱"]["唱片"] = 5
        self.group["乐谱"]["海报"] = 0
        self.group["唱片"] = {}
        self.group["唱片"]["吉他"] = 15
        self.group["唱片"]["架子鼓"] = 20
        self.group["海报"] = {}
        self.group["海报"]["吉他"] = 30
        self.group["海报"]["架子鼓"] = 35
        self.group["吉他"] = {}
        self.group["吉他"]["钢琴"] = 20
        self.group["架子鼓"] = {}
        self.group["架子鼓"]["钢琴"] = 10
        self.group["钢琴"] = {}

    def creat_price_list(self):
        self.price[self.start] = 0
        for article in self.group:
            if article != self.start:
                self.price[article] = MAX

    def visit_point(self):
        self.father = {}
        for article in self.group[self.start]:
            self.queue += [[article, self.start]]
        while self.queue:
            this_point, father = self.queue.popleft()
            if self.price[father] + self.group[father][this_point] < self.price[this_point]:
                self.price[this_point] = self.price[father] + self.group[father][this_point]
                self.father[this_point] = father
            for article in self.group[this_point]:
                self.queue += [[article, this_point]]

    def Print_list(self):
        print (self.price)
        print (self.father)
        temp = "钢琴"
        while True:
            print (temp)
            try:
                temp = self.father[temp]
            except:
                break


a = Exchange_piano()
a.create_group()
a.creat_price_list()
a.visit_point()
a.Print_list()