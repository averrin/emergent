function chat_send(editor){
    $.post("/activity/send", {message: editor.exportFile()}, function(){
        editor.importFile();
    });
}

$(function(){

    var chat_message = _.template(
        "<div class='chat_message'>" +
            "<strong><a href='/users/<%= user %>'><%= user %></a></strong> (<%= now %>): <br>" +
            " <%= message %>" +
         "</div>"
    );
    var rpg_message = _.template(
        "<div class='rpg_message'>" +
            " <%= message %>" +
         "</div>"
    );
    
    function ws_handler(data) {
        console.log(data);
        data.now = new Date().toLocaleTimeString();
        var template;
        if(data.type == "chat"){
            template = chat_message;
        }else if(data.type == "rpg"){
            template = rpg_message;
        }
        $("#events").append(template(data));
    }

    websocket_init(ws_handler);

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
    
    $.get("/activity/history", function(data){
        console.log(data);
        _.each(data.history, function(e,i){
            e.now = new Date().toLocaleTimeString();
            var template;
            if(e.type == "chat"){
                template = chat_message;
            }else if(e.type == "rpg"){
                template = rpg_message;
            }
            $("#events").append(template(e));    
        })
        
    })
});
