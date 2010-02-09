import ctypes

_hello = ctypes.CDLL("lib/libhello.so")
_hello.hello.restype = ctypes.c_int
_hello.hello.argtypes = []

def hello():
    print('Hello from Hello.py')

def hello2():
    _hello.hello()

if __name__ == '__main__':
    hello()
    hello2()
