function websocket_init(){
    var pusher = new Pusher('6bb5412badf09454aa87');
        var channel = pusher.subscribe('activity');
        channel.bind('my_event', function(data) {
            console.log(data);
            data.now = new Date().toLocaleTimeString();
            $("#events").append(chat_message(data));
        });
    
}