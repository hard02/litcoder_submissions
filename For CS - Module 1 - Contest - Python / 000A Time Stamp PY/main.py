from bisect import bisect_right
from collections import defaultdict

class TimeTravelersArchive:
    def __init__(self):
        self.data = defaultdict(list)

    def Store(self, key, value, timestamp):
        self.data[key].append((timestamp, value))

    def Retrieve(self, key, timestamp):
        if not self.data[key]:
            print("Wrong method called, please call Store or Retrieve method")
            return ""

        index = bisect_right(self.data[key], (timestamp, chr(127)))
        if index > 0:
            return self.data[key][index - 1][1]
        else:
            return "empty"

# Input
archive = TimeTravelersArchive()

try:
    while True:
        query = input().split()
        if query[0] == "Store":
            archive.Store(query[1], query[2], int(query[3]))
        elif query[0] == "Retrieve":
            result = archive.Retrieve(query[1], int(query[2]))
            print(result)
        else:
            print("Invalid input")
except EOFError:
    pass

