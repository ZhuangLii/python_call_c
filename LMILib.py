import ctypes
from ctypes import *

#lib = ctypes.cdll.LoadLibrary("/home/stq/Desktop/GO_SDK/lib/linux_x64d/libGoSdk.so")
lib = ctypes.cdll.LoadLibrary('/home/stq/Desktop/libLMI.so')

class LMI(object):
    def __init__(self):
        
        lib.lmi_init.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.lmi_init.restype = ctypes.c_int

        lib.lmi_grap.argtypes = [ctypes.c_void_p]
        lib.lmi_grap.restype = ctypes.c_int
        
        lib.lmi_del.argtypes = [ctypes.c_void_p]
        lib.lmi_del.restype = ctypes.c_int

        self.obj = lib.lmi_new()


    def init(self, val):
        return lib.lmi_init(self.obj, val)


    def grap(self):
        return lib.lmi_grap(self.obj)
        
    def __del__(self):
        return lib.lmi_del(self.obj)

def main():
    lmi = LMI()
    a = bytes("123",encoding='utf-8')
    lmi.init(a)


if __name__ == '__main__':
    main()