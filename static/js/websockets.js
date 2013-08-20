function websocket_init(ws_handler){
    var pusher = new Pusher('6bb5412badf09454aa87');
        var channel = pusher.subscribe('activity');
        channel.bind('my_event', ws_handler);
    
}