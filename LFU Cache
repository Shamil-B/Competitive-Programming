class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cnt = {}
        self.nodes = {}
        self.counter = []

    def get(self, key: int) -> int:
        if key in self.nodes:
            self.cnt[key] += 1
            if self.cnt[key]-1 < len(self.counter):
                self.counter[self.cnt[key]-2].remove(key)
                self.counter[self.cnt[key]-1].append(key)
            else:
                self.counter[self.cnt[key]-2].remove(key)
                self.counter.append([key])
            return self.nodes[key]
        return -1

    def put(self, key: int, value: int) -> None:

        if len(self.nodes)<self.capacity or key in self.nodes:
            self.nodes[key] = value
            if key in self.cnt:
                self.cnt[key] += 1
                if self.cnt[key]-1 < len(self.counter):
                    self.counter[self.cnt[key]-2].remove(key)
                    self.counter[self.cnt[key]-1].append(key)
                else:
                    self.counter[self.cnt[key]-2].remove(key)
                    self.counter.append([key])
            else:
                self.cnt[key] = 1
                if self.cnt[key]-1 < len(self.counter):
                    self.counter[self.cnt[key]-1].append(key)
                else:
                    self.counter.append([key])

        else:
            invalids = None
            for ls in self.counter:
                if ls:
                    invalids = ls
                    break
            keyToRemove = None

            if invalids:
                keyToRemove = invalids[0]


            if keyToRemove!=None:
                self.nodes.pop(keyToRemove)
                self.counter[self.cnt[keyToRemove]-1].remove(keyToRemove)
                self.cnt.pop(keyToRemove)
                self.put(key,value)

