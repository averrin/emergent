$(".level_info").tooltip({placement: "bottom", html: true})

var pusher = new Pusher('6bb5412badf09454aa87');
    var channel = pusher.subscribe('activity');
    channel.bind('my_event', function(data) {
        console.log(data)
        var now = new Date().toLocaleTimeString();
        $("#events").append(data.user + ' (' + now + "): " + data.message + "<br>");
        $("#msg_text").val("")
    });

$("#msg_form").on("submit", function(e){
	e.preventDefault();
	$.post("/activity/send", {message:$('#msg_text').val()}, function(){})
	$('#msg_text').val('')
	return false;
})
