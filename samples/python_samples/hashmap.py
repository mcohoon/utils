

Class DictMap:

    def __init__(self):
        newDictMap = [];

    def put(self, key, value):
        keyIndex = self.hash(key)
        self.newDictMap[keyIndex].append(key, value)
        
    def get(self, key):
        keyIndex = self.hash(key)
        for i in self.newDictMap[keyIndex]:
            if i == key:
                return key,value
        return None
