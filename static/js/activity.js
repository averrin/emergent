function chat_send(editor){
    $.post("/activity/send", {message: editor.exportFile()}, function(){
        editor.importFile();
    });
}

$(function(){

    var templates = { 
	chat:  _.template(
        "<div class='chat_message'>" +
            "<strong><a href='/users/<%= user %>'><%= user %></a></strong> (<%= now.toLocaleDateString() %> <%= now.toLocaleTimeString() %>): <br>" +
            " <%= message %>" +
         "</div>"
    	),
    	rpg:  _.template(
        "<div class='rpg_message'>" +
            " <%= message %>" +
         "</div>"
	)
    }
    
    function ws_handler(data) {
        data.now = new Date(data.timestamp);
	    var ev = $("#events");
        ev.append(templates[data.type](data));
	    ev.animate({scrollTop: ev.prop("scrollHeight")}, 500);
	    $('#events div:last-child').addClass('animated bounceInLeft');
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
            e.now = new Date(e.timestamp);
            $("#events").append(templates[e.type](e));    
        })
        
    })
});
