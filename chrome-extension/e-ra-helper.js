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
})
