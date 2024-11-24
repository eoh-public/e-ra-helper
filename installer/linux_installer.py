import json
import os
import sys
import webbrowser

# pyinstaller
if getattr(sys, 'frozen', False):
    current_folder = os.path.dirname(os.path.abspath(sys.executable))
else:
    current_folder = os.path.dirname(os.path.abspath(__file__))


desktop_json_path = 'com.eoh.era_helper_desktop.json'

print('register native message host with chrome')
with open(os.path.join(current_folder, desktop_json_path), 'r') as f:
    desktop_json = json.load(f)

desktop_json['path'] = os.path.join(current_folder, 'e-ra-helper')

with open(f'{os.environ["HOME"]}/.config/google-chrome/NativeMessagingHosts/com.eoh.era_helper_desktop.json', 'w') as f:
    json.dump(desktop_json, f, indent=4)

print('install ffmpeg')
os.system('apt install -y ffmpeg')

print('install chrome extension')
chrome_extension_url = 'https://chrome.google.com/webstore/detail/e-ra-helper/ppihjimjhbokffindbgmmopjfcmhhelh'
webbrowser.open(chrome_extension_url)
