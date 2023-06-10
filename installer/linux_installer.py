import json
import os

desktop_json_path = 'native-messaging-host/com.eoh.era_helper_desktop.json'

current_folder = os.path.realpath(os.path.dirname(__file__))
# modify native message hot path
with open(desktop_json_path, 'r') as f:
    desktop_json = json.load(f)

desktop_json['path'] = os.path.join(current_folder, 'e-ra-helper')

# register native message host with chrome
with open(f'{os.environ["HOME"]}/.config/google-chrome/NativeMessagingHosts/com.eoh.era_helper_desktop.json', 'w') as f:
    json.dump(desktop_json, f, indent=4)

# install chrome extension
chrome_extension_url = 'https://chrome.google.com/webstore/detail/e-ra-helper/ppihjimjhbokffindbgmmopjfcmhhelh'
os.system(f'google-chrome {chrome_extension_url}')
