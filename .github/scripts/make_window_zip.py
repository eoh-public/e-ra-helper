from zipfile import ZipFile

with ZipFile('e-ra-helper-window.zip', 'w') as zip_object:
   zip_object.write('dist/e-ra-helper.exe', 'e-ra-helper.exe')
   zip_object.write('dist/window_installer.exe', 'window_installer.exe')
   zip_object.write('native-messaging-host/com.eoh.era_helper_desktop.json', 'com.eoh.era_helper_desktop.json')
