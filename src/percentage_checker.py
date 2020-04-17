
class PercentChecker:
    def __init__(self, max_size: int):
        self.num_counted = 0
        self.max_size = max_size
    
    def increased_percent(self):
        self.increase(1)
        return round(self._percent(), 4)
    
    def increase(self, count: int):
        self.num_counted += count

    def _percent(self):
        return (float(self.num_counted) / float(self.max_size)) * 100