import datetime


class PrintLog:
    def __init__(self, filename):
        self.filename = filename

    def date_format(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_log(self, msg, is_print_msg=True):
        with open(self.filename, "a", encoding="utf8") as f:
            f.write("{} {}".format(self.date_format(), msg + "\n"))
        if is_print_msg:
            print(msg)
