import json
import os
import struct
import sys
from ctypes import WinDLL
from datetime import datetime

import requests

window_x = struct.calcsize("P") * 8

if getattr(sys, 'frozen', False):
    current_folder = os.path.dirname(os.path.abspath(sys.executable))
else:
    current_folder = os.path.dirname(os.path.abspath(__file__))

dll_path = os.path.join(os.path.dirname(__file__), 'CardEncoder', 'dll', str(window_x), 'CardEncoder.dll')
card_encoder = WinDLL(dll_path)

with open(os.path.join(current_folder, 'configuration.json')) as f:
    configuration = json.load(f)


def issue_card():
    building_number = int(sys.argv[2])
    floor_number = int(sys.argv[3])
    mac_address = sys.argv[4]
    expired_time = int(sys.argv[5])

    print('Get hotel info')
    response = requests.get('https://euapi.ttlock.com/v3/hotel/getInfo', params={
        'clientId': configuration['client_id'],
        'clientSecret': configuration['client_secret'],
        'date': datetime.now().timestamp() * 1000
    })
    hotel_info = response.json()['hotelInfo']

    print('Connect to card encoder')
    result = card_encoder.CE_ConnectComm(configuration['port_name'].encode())
    print(result)

    print('Init card encoder')
    result = card_encoder.CE_InitCardEncoder(hotel_info.encode())
    print(result)

    print('Init card')
    result = card_encoder.CE_InitCard(hotel_info.encode())
    print(result)

    print('Write card')
    result2 = card_encoder.CE_WriteCard(
        hotel_info.encode(),
        building_number,
        floor_number,
        mac_address.replace(':', '').encode(),
        expired_time,
        1,
    )
    print(result2)


def main():
    issue_card()


if __name__ == '__main__':
    main()
