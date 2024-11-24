window.postMessage({
  message: 'e-ra-helper-ready',
});

window.addEventListener('message', (event) => {
  if (!event.data) {
    return;
  }
  switch (event.data.type) {
    case 'open_in_vlc_player':
      console.log(`Playing in VLC player URI ${event.data.uri}`);
      chrome.runtime.sendMessage({
        message: {
          type: 'open_in_vlc_player',
          uri: event.data.uri,
        },
      });
      break;
    case 'ttlock_issue_card_offline':
      console.log('ttlock_issue_card_offline', event.data);
      chrome.runtime.sendMessage({
        message: {
          type: 'ttlock_issue_card_offline',
          lock: event.data.lock,
        },
      });
      break;
    default:
      break;
  }
});


setInterval(() => {
  const elements = document.getElementsByClassName('rtsp_uri');
  if (!elements?.length) {
    chrome.runtime.sendMessage({
      message: {
        type: 'stop_local_server',
      },
    });
    return;
  }
  for (let i = 0; i < elements.length; i++) {
    const element = elements[i];
    const uri = element.getElementsByTagName('input')[0].value;
    const parent = element.parentNode;
    const container = parent.parentNode;
    const wrapper = container.parentNode.parentNode
    if (container.className.includes('helper-processed')) {
      continue;
    }

    chrome.runtime.sendMessage({
      message: {
        type: 'start_local_server',
      },
    });

    const widgetId = wrapper.id.split('_')[1];

    chrome.runtime.sendMessage({
      message: {
        type: 'rtsp_start_conversion',
        uri: uri,
        widgetId: widgetId,
      },
    });

    parent.style.display = 'none';
    container.className += ' helper-processed';

    const iframe = document.createElement('iframe');
    iframe.src = `http://localhost:9999/test.html?id=` + widgetId;
    iframe.style.width = '100%'
    iframe.style.height = '100%'

    container.appendChild(iframe);
  }
}, 1000);
