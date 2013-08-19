$(function(){
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
	$.post("/activity/send", {message: editor.exportFile()}, function(){})
	editor.importFile()
	return false;
})
});
