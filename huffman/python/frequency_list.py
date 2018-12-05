class FrequencyList:
    def __init__(self, data):
        self.list = {}
        for datum in data:
            if datum not in self.list:
                self.list[datum] = 0
            self.list[datum] += 1

    def __str__(self):
        temp = "%-20s: %20s\n" % ("key", "value")
        for key, value in self.list.items():
            temp += "%-20s: %20s\n" % (key, value)
        return temp
