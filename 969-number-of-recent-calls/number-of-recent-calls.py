class RecentCounter:

    def __init__(self):
        self.requests = []
        self.timer = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[self.timer] < t-3000:
            self.timer += 1
        return len(self.requests) - self.timer




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)