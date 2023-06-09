window.postMessage({
    message: 'e-ra-helper-ready',
});

window.addEventListener('message', (event) => {
    if (event.data && event.data.type === 'open_in_vlc_player') {
        console.log(`Playing in VLC player URI ${event.data.uri}`);
        chrome.runtime.sendMessage({
            message: {
                type: 'open_in_vlc_player',
                uri: event.data.uri,
            },
        });
    }
})