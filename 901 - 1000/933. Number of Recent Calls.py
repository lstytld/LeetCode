class RecentCounter:

    def __init__(self):
        self.pings = []
        self.length = 0

    def ping(self, t: int) -> int:
        self.pings.append(t)
        self.length += 1
        while self.pings[0] < (t - 3000):
            self.pings.pop(0)
            self.length -= 1
        return self.length

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
