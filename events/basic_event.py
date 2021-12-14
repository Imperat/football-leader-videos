class BasicEvent:
    def __init__(self):
        self.time = 0

    def set_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

    def get_duration(self, all_future_events):
        pass
