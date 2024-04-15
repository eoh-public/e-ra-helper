import os
from ctypes import WinDLL
import struct
window_x = struct.calcsize("P") * 8

dll_path = os.path.join(os.path.dirname(__file__), 'CardEncoder', 'dll', str(window_x), 'CardEncoder.dll')
card_encoder = WinDLL(dll_path)

hotel_info = '{}'


def issue_card_via_encoder():
    result = card_encoder.CE_ConnectCommOnPromise('COM1', 0)
    print(result)

    result = card_encoder.CE_InitCardEncoder(hotel_info)
    print(result)

    result2 = card_encoder.CE_WriteCard("{}", 1, 1, "001325ABC87E", 0, 1)
    print(result2)
