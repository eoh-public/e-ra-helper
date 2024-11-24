chrome.runtime.onMessage.addListener(
  function (request, sender, sendResponse) {
    switch (request.message.type) {
      case 'open_in_vlc_player':
        console.log(`Playing in VLC player URI ${request.message.uri}`);
        chrome.runtime.sendNativeMessage('com.eoh.era_helper_desktop', {
          type: 'open_in_vlc_player',
          uri: request.message.uri,
        }, function (response) {
          console.log('Received ' + response);
        })
        break;
      case 'rtsp_start_conversion':
        console.log(`rtsp_start_conversion URI ${request.message.uri}`);
        chrome.runtime.sendNativeMessage('com.eoh.era_helper_desktop', {
          type: 'rtsp_start_conversion',
          uri: request.message.uri,
          widgetId: request.message.widgetId,
        }, function (response) {
          console.log('Received ' + response);
        })
        break;
      case 'start_local_server':
        console.log(`start_local_server`);
        chrome.runtime.sendNativeMessage('com.eoh.era_helper_desktop', {
          type: 'start_local_server',
        }, function (response) {
          console.log('Received ' + response);
        })
        break;
      case 'stop_local_server':
        console.log(`stop_local_server`);
        chrome.runtime.sendNativeMessage('com.eoh.era_helper_desktop', {
          type: 'stop_local_server',
        }, function (response) {
          console.log('Received ' + response);
        })
        break;
      case 'ttlock_issue_card_offline':
        console.log('ttlock_issue_card_offline', request.message.lock);
        chrome.runtime.sendNativeMessage('com.eoh.era_helper_desktop', {
          type: 'ttlock_issue_card_offline',
          mac_address: request.message.lock.mac_address,
          floor_number: request.message.lock.floor_number,
          building_number: request.message.lock.building_number,
        }, function (response) {
          console.log('Received ' + response);
        })
        break;
      default:
        break;
    }
    sendResponse({type: 'service_worker_received'});
  }
);
