from zipfile import ZipFile

with ZipFile('window.zip', 'w') as zip_object:
   zip_object.write('dist/e-ra-helper/e-ra-helper.exe', 'e-ra-helper.exe')
   zip_object.write('dist/linux_installer/linux_installer.exe', 'linux_installer.exe')
   zip_object.write('native-messaging-host/com.eoh.era_helper_desktop.json', 'com.eoh.era_helper_desktop.json')
