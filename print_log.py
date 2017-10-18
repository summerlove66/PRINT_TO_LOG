import datetime

class PrintLog:
    def __init__(self, filename):
        self.filename = filename

    def date_format(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_log(self, msg):
        with open(self.filename, "a" ,encoding="utf8") as f:
            f.write("{} {}".format(self.date_format(), msg))
        print(msg)


