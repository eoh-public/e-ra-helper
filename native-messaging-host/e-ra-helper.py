import json
import platform
import subprocess
from datetime import datetime

import nativemessaging

is_window = platform.system() == 'Windows'

try:
    message = nativemessaging.get_message()
    if message:
        with open("log.txt", "a") as f:
            f.write(json.dumps(message) + "\n")

    if message['type'] == 'open_in_vlc_player':
        # start vlc player
        if is_window:
            subprocess.Popen(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe', message['uri']], shell=True)
        else:
            subprocess.Popen(['vlc', message['uri']], shell=True)
        with open("log.txt", "a") as f:
            f.write("Start vlc\n")

        nativemessaging.send_message(nativemessaging.encode_message('Start vlc'))

    if message['type'] == 'ttlock_issue_card_offline':
        output = subprocess.check_output(
            [
                'C:\\Users\\daotr\\PycharmProjects\\e-ra-helper\\ttlock_encoder\\dist\\ttlock_encoder.exe',
                'issue_card',
                str(message['building_number']),
                str(message['floor_number']),
                message['mac_address'],
                str(int(datetime.now().timestamp()) + 60 * 60 * 24 * 30)
            ],
            shell=True)

        with open("log.txt", "a") as f:
            f.write("Start issuing the card\n")
            f.write(f"{output}\n")

        nativemessaging.send_message(nativemessaging.encode_message('Start issuing the card'))
except Exception as ex:
    with open("log.txt", "a") as f:
        f.write(str(ex) + "\n")
