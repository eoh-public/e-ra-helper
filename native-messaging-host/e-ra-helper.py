import json
import platform
import subprocess

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
        subprocess.Popen(
            ['issue_card_via_encoder', message['building_number'], message['floor_number'], message['mac_address']],
            shell=True)
        with open("log.txt", "a") as f:
            f.write("Start vlc\n")
        nativemessaging.send_message(nativemessaging.encode_message('Start issuing the card'))
except Exception as ex:
    with open("log.txt", "a") as f:
        f.write(str(ex) + "\n")
