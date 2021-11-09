
class Time:

    def __init__(self, hour, minute, second=0, m_second=0) -> int:
        self.hour = hour
        self.minute = minute
        self.second = second
        self.m_second = m_second

    def to_seconds(self):
        seconds = ((self.hour * 3600) + (self.minute * 60) + (self.m_second / 1000) + self.second)
        return seconds

    def from_seconds(self, seconds:float):
        hour = int(seconds // 3600)
        minutes = int(seconds // 60)
        second = int(seconds - ((hour * 3600) + (minutes * 60)))
        m_seconds = (seconds - ((hour * 3600) + (minutes * 60) + second)) * 1000
        return f"{str(hour).zfill(2)}:{str(minutes).zfill(2)}:{str(second).zfill(2)}.{m_seconds}"

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}:{str(self.second).zfill(2)}.{self.m_second}"

    def __eq__(self, other):
        return self.to_seconds() == other

    def __add__(self, other):
        total_hour = self.hour + other.hour
        total_minute = self.minute + other.minute
        total_second = self.second + other.second
        total_m_second = self.m_second + other.m_second
        return Time(total_hour, total_minute, total_second, total_m_second)


class DateTime(Time):

    def __init__(self, year, month, day):
        super().__init__()
        self.year = year
        self.month = month
        self.day = day

    def to_seconds(self):
        return super().to_seconds()

    def __eq__(self, other):
        return self.to_seconds() == other

    def __add__(self, other):
        super().__add__()

        return DateTime(self.year, self.month, self.day)

    def __str__(self):
        return f"{str(self.year).zfill(4)}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)} {str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}:{str(self.second).zfill(2)}.{self.m_second}"







t1 = Time(5, 3, 20, 150)
print(t1.__str__())