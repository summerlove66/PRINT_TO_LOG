from print_log import PrintLog
from print_log_decorator  import print_to_log

@print_to_log("test3.txt")
def test_1(x):

    print(x)
    print("test1写入日志")
    return x

def test_2():
    print = PrintLog("test1.txt").to_log
    print("test_2不写入")

a =test_1("kaixin")
test_2()
print(a)