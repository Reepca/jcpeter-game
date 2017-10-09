class jArray(object):
    def __init__(self, capacity=30, startValues=None):
        self.data = list()
        self.capacity = capacity
        self.startValues = startValues
        self.data = [startValues for i in range(capacity)]
        
    def __setitem__(self, index, newValue):
        self.data[index] = newValue
        
    def __getitem__(self, index):
        return self.data[index]
    
    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        return iter(self.data)