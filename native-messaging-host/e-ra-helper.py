import json
import subprocess

import nativemessaging

try:
    message = nativemessaging.get_message()
    if message:
        with open("log.txt", "a") as f:
            f.write(json.dumps(message) + "\n")

    if message['type'] == 'open_in_vlc_player':
        # start vlc player
        subprocess.Popen(['vlc', message['uri']], shell=True)
        with open("log.txt", "a") as f:
            f.write("Start vlc\n")
except Exception as ex:
    with open("log.txt", "a") as f:
        f.write(str(ex) + "\n")
