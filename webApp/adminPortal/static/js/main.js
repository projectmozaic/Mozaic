// if dropzone exist
Dropzone.autoDiscover = false;
$(document).ready(function() {
    if ($('.dropzone').length > 0) {

        $(".dropzone").dropzone({
            url: "success",
			uploadMultiple: true,
            addRemoveLinks: true,
            autoProcessQueue: false,
            dictResponseError: 'File Upload Error.',
			dictDefaultMessage: 'Drop datasets here to upload',
			init: function() {
                var zone = this;
                $('#generate').click(function(){
                        zone.processQueue();
                });
			}
        });
    } // end if dropzone exist
});