// if dropzone exist
Dropzone.autoDiscover = false;
$(document).ready(function() {
    if ($('.dropzone').length > 0) {

        $(".dropzone").dropzone({
            url: "generate",
			uploadMultiple: true,
            addRemoveLinks: true,
            autoProcessQueue: false,
            dictResponseError: 'File Upload Error.',
			dictDefaultMessage: 'Drop datasets here to upload',
			init: function() {
                var zone = this;
                $('#create').click(function(){
                        zone.processQueue();
                });
			}
        });
    } // end if dropzone exist

    $(".lang").click(function(){
        var item = $(this).parent().parent().parent().next().find("input").prop('disabled', function(i, v) { return !v; });
        console.log(item);
    });
});


//code for dynamic form fields
//http://bootsnipp.com/snippets/featured/dynamic-form-fields-add-amp-remove
$(document).ready(function(){
    var next = 1;
    $(".add-more").click(function(e){
        e.preventDefault();
        var addto = "#field" + next;
        var addRemove = "#field" + (next);
        next = next + 1;
        var newIn = '<input autocomplete="off" class="input form-control" id="field' + next + '" name="field' + next + '" type="text">';
        var newInput = $(newIn);
        var removeBtn = '<button id="remove' + (next - 1) + '" class="btn btn-danger remove-me" >-</button></div><div id="field">';
        var removeButton = $(removeBtn);
        $(addto).after(newInput);
        $(addRemove).after(removeButton);
        $("#field" + next).attr('data-source',$(addto).attr('data-source'));
        $("#count").val(next);  
        
            $('.remove-me').click(function(e){
                e.preventDefault();
                var fieldNum = this.id.replace("remove","")
                var fieldID = "#field" + fieldNum;
                $(this).remove();
                $(fieldID).remove();
            });
    });
});