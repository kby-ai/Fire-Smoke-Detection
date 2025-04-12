import os

from ctypes import *

libPath = os.path.abspath(os.path.dirname(__file__)) + '/libfire.so'
firesdk = cdll.LoadLibrary(libPath)

getMachineCode = firesdk.getMachineCode
getMachineCode.argtypes = []
getMachineCode.restype = c_char_p

setActivation = firesdk.setActivation
setActivation.argtypes = [c_char_p]
setActivation.restype = c_int32

initSDK = firesdk.initSDK
initSDK.argtypes = []
initSDK.restype = c_int32

getFireDetection = firesdk.get_fire_using_bytes
getFireDetection.argtypes = [c_char_p, c_ulong, POINTER(c_int), POINTER(c_int), POINTER(c_float)]
getFireDetection.restype = c_int32