// if dropzone exist
Dropzone.autoDiscover = false;
$(document).ready(function() {
    if ($('#fileZone').length > 0) {

        $("#fileZone").dropzone({
            url: "generate",
			uploadMultiple: true,
            addRemoveLinks: true,
            clickable: "#previewZone",
            previewsContainer: "#previewZone",
            autoProcessQueue: false,
            dictResponseError: 'File Upload Error.',
			dictDefaultMessage: 'Drop datasets here to upload',
			init: function() {
                var zone = this;
                $('#create').click(function(e){
                    e.preventDefault();
                    e.stopPropagation();
                    zone.processQueue();
                });

                this.on("addedfile", function(file) {
                    $(".dz-default").hide();
                });

                this.on("removedfile", function(file) {
                    if (zone.getQueuedFiles().length == 0) {
                        $(".dz-default").show();
                    }
                });
			}
        });
    } // end if dropzone exist

    $(".lang").click(function(){
        var item = $(this).parent().parent().parent().next().find("input").prop('disabled', function(i, v) { return !v; });
        console.log(item);
    });

    $(document).on("click", ".addRepo", function (e) {
        e.preventDefault();
        $(this).toggleClass('addRepo removeRepo');
        $(this).html('<i class="fa fa-minus" aria-hidden="true"></i>');
        var addElement = '<div class="input-group"> <input type="text" name="gitRepo" class="form-control" placeholder="Git Repo..."> \
                <span class="input-group-btn"> \
                <button class="btn btn-secondary addRepo" type="button"><i class="fa fa-plus" aria-hidden="true"></i></button>\
                </span>\
            </div>';
        var item = $(this).parent().parent();
        item.after(addElement);

    });

    $(document).on("click", ".removeRepo", function (e) {
        e.preventDefault();
        var item = $(this).parent().parent();
        console.log(item);
        $(this).parent().parent().remove();

    });

    $(document).on("click", ".addAptget", function (e) {
        e.preventDefault();
        $(this).toggleClass('addAptget removeAptget');
        $(this).html('<i class="fa fa-minus" aria-hidden="true"></i>');
        var addElement = '<div class="input-group"> <input type="text" name="aptget" class="form-control" placeholder="Package Name"> \
                <span class="input-group-btn"> \
                <button class="btn btn-secondary addAptget" type="button"><i class="fa fa-plus" aria-hidden="true"></i></button>\
                </span>\
            </div>';
        var item = $(this).parent().parent();
        item.after(addElement);

    });

    $(document).on("click", ".removeAptget", function (e) {
        e.preventDefault();
        var item = $(this).parent().parent();
        console.log(item);
        $(this).parent().parent().remove();

    });
});




