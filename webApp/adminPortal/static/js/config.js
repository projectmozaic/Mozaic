$(document).ready(function(){
	$('#filebutton').on('change', ':file', function(){
        var input = $(this);
        label = input.val().replace(/^.*?([^\\\/]*)$/, '$1');
        document.getElementById("packagefile").value = label;
    });

    $(':file').change(function(){
    	if (this.files && this.files[0]){
    		var reader = new FileReader();
    		reader.onload = function(e){
    			json = JSON.parse(e.target.result);
    			$("#configinput").text(JSON.stringify(json));
    		};
    		$("configinput").text(reader.readAsText(this.files[0]));
    	}
    });
    
});