function chat_send(editor){
        $.post("/activity/send", {message: editor.exportFile()}, function(){
            editor.importFile();
        });
}

$(function(){

    var chat_message = _.template("<div class='chat_message'><strong><a href='/users/<%= user %>'><%= user %></a></strong> (<%= now %>): <br> <%= message %></div>")

    var pusher = new Pusher('6bb5412badf09454aa87');
        var channel = pusher.subscribe('activity');
        channel.bind('my_event', function(data) {
            console.log(data);
            var now = new Date().toLocaleTimeString();
            data.now = now;
            $("#events").append(chat_message(data));
        });
    
    var editor = new EpicEditor({
    
    theme: {
        base: "http://"+location.host+'/static/epiceditor/themes/base/epiceditor.css',
        preview: "http://"+location.host+'/static/epiceditor/themes/preview/preview-dark.css',
        editor: "http://"+location.host+'/static/epiceditor/themes/editor/epic-dark.css'
      },
    focusOnLoad: true
    }).load();
    
    $("#msg_form").on("submit", function(e){
        e.preventDefault();
        chat_send(editor);        
        return false;
    });
    
    //TODO: shortcut in editor
    Mousetrap.bind(['ctrl+enter'], function(e) {
        console.log("Ctrl + Enter");
        chat_send(editor);
    });
});
