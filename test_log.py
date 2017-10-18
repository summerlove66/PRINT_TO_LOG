from print_log import PrintLog
from print_log_decorator  import print_to_log


@print_to_log("test.log")
def test_1(x):

    print(x)
    print("test1 to log")
    return x

def test_2():
    print = PrintLog("test1.log").to_log
    print("test_2 not to log")
def test_3 ():
    print("test3")


a =test_1("testing")
test_2()
test_3()