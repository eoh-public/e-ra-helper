import json
import os
import platform
import shutil
import subprocess
import http.server
from datetime import datetime


import nativemessaging
import psutil

is_window = platform.system() == 'Windows'


def main():
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

        if message['type'] == 'rtsp_start_conversion':
            widget_id = int(message['widgetId'])
            rtsp_uri = message['uri']

            if os.path.isdir(str(widget_id)):
                with open(f"{widget_id}/ffmpeg.pid", "r") as f:
                    pid = int(f.read())

                try:
                    process = psutil.Process(pid)
                    if process.status() == 'running':
                        return
                except psutil.NoSuchProcess:
                    pass

                shutil.rmtree(str(widget_id))
            os.makedirs(str(widget_id), exist_ok=True)

            command = 'ffmpeg'
            if is_window:
                command = os.path.join(".", "ffmpeg")

            command = (f'{command} -fflags nobuffer -loglevel debug -rtsp_transport tcp '
                       f'-i {rtsp_uri} '
                       f'-vsync 0 -copyts -vcodec copy -movflags frag_keyframe+empty_moov -an '
                       f'-hls_flags delete_segments+append_list -f hls -hls_time 10 -hls_list_size 3 '
                       f'-hls_segment_type mpegts ./{widget_id}/index.m3u8')

            process = subprocess.Popen(command.split(' '), shell=True)
            with open(f"{widget_id}/ffmpeg.pid", "w") as f:
                f.write(str(process.pid))
            with open("log.txt", "a") as f:
                f.write(f"Started ffmpeg {rtsp_uri}\n")

            nativemessaging.send_message(nativemessaging.encode_message('started rtsp conversion'))

        if message['type'] == 'start_local_server':
            current_pid = os.getpid()
            try:
                with open('local-server.txt', 'r') as f:
                    old_pid = int(f.read())
            except FileNotFoundError:
                old_pid = None

            if old_pid:
                try:
                    process = psutil.Process(old_pid)
                    if process.status() == 'running':
                        return
                except psutil.NoSuchProcess:
                    pass
            with open('local-server.txt', 'w') as f:
                f.write(str(current_pid))

            server = http.server.HTTPServer(('localhost', 9999), http.server.SimpleHTTPRequestHandler)
            server.serve_forever()

        if message['type'] == 'stop_local_server':
            try:
                with open('local-server.txt', 'r') as f:
                    old_pid = int(f.read())
            except FileNotFoundError:
                old_pid = None
            if old_pid:
                try:
                    process = psutil.Process(old_pid)
                    if process.status() == 'running':
                        process.kill()
                except psutil.NoSuchProcess:
                    pass
            nativemessaging.send_message(nativemessaging.encode_message('stop_local_server'))

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


if __name__ == '__main__':
    main()
