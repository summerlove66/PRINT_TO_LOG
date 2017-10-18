import sys

def print_to_log(filename):
    def to_log(f):
        def wapper(*args ,**kw):
            res =f(*args ,**kw)
            sys.stdout = raw_stdout
            return res
        return wapper
    raw_stdout = sys.stdout
    sys.stdout = open(filename ,"a" ,encoding="utf8")
    return to_log