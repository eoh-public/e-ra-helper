from zipfile import ZipFile

with ZipFile('e-ra-helper-linux.zip', 'w') as zip_object:
   zip_object.write('dist/e-ra-helper', 'e-ra-helper')
   zip_object.write('dist/linux_installer', 'linux_installer')
   zip_object.write('native-messaging-host/com.eoh.era_helper_desktop.json', 'com.eoh.era_helper_desktop.json')
