chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        chrome.runtime.sendNativeMessage('com.eoh.era_helper_desktop', {
            type: 'open_in_vlc_player',
            uri: request.message.uri,
        }, function(response) {
            console.log('Received ' + response);
        })
        sendResponse({type: 'service_worker_recieved'});
    }
  );