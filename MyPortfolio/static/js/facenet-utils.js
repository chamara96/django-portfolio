$(document).ready(function (e) {

    var $loading = $('#ajaxloader').hide();
    $(document).ajaxStart(function () {
        $loading.show();
    }).ajaxStop(function () {
        $loading.hide();
    });

    $('.custom-file-input').on('change', function (e) {
        //get the file name
        var fileName = e.target.files[0].name;
        //replace the "Choose a file" label
        $(this).next('.custom-file-label').html(fileName);
        showPreview(e);
    });

    // Variable to hold request
    var request;

    $("#image-process-form").on('submit', function (e) {
        e.preventDefault();

        if (request) {
            request.abort();
        }
        var $form = $(this);
        var $inputs = $form.find("input, button");

        $.ajax({
            type: 'POST',
            url: process_image_url,
            data: new FormData(this),
            dataType: 'json',
            contentType: false,
            cache: false,
            processData: false,
            beforeSend: function () {
                $inputs.prop("disabled", true);
            },
            success: function (response) {
                var face_count = response["faces"].length;
                var face_names = [];
                response["faces"].forEach(face => {
                    drawBoundryBoxWithName(face["box"], face["name"]);
                    face_names.push(face["name"]);
                });
                $("#image-process-form .messages").html(face_count + " faces identified <br>" + face_names.join(", "));
            },
            error: function (jqXHR, textStatus, errorThrown) {
                $("#image-process-form .messages").text(errorThrown);
            },
            complete: function (jqXHR, textStatus) {
                $inputs.prop("disabled", false);
            }
        });
    });


    $("#face-train-form").on('submit', function (e) {
        e.preventDefault();

        if (request) {
            request.abort();
        }
        var $form = $(this);
        var $inputs = $form.find("input, button");

        $.ajax({
            type: 'POST',
            url: train_face_url,
            data: new FormData(this),
            dataType: 'json',
            contentType: false,
            cache: false,
            processData: false,
            beforeSend: function () {
                $inputs.prop("disabled", true);
            },
            success: function (response) {
                var name = response["trained_face"]["name"];
                $("#face-train-form .messages").text(name + ", Your face vector has added to the system.");
                drawBoundryBoxWithName(response["trained_face"]["box"], response["trained_face"]["name"]);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                var msg = errorThrown + ". <br> ";
                error_res = jqXHR.responseJSON;
                for (let key in error_res) {
                    if (error_res.hasOwnProperty(key)) {
                        msg += key + ": " + error_res[key] + ".";
                    }
                }
                $("#face-train-form .messages").html(msg);
            },
            complete: function (jqXHR, textStatus) {
                $inputs.prop("disabled", false);
            }
        });
    });

});


var canvas = document.getElementById('canvas');
var canvas_parent = document.getElementById('canvas-parent');
canvas.width = canvas_parent.clientWidth;

var ctx = canvas.getContext('2d');

img = new Image();

function openImageOnCanvas(imgBlobURL) {
    img.src = imgBlobURL;

    img.onload = function () {
        // Get the canvas' current style
        var canvasStyle = getComputedStyle(canvas);
        // Get it's current width, minus the px at the end
        var canvasWidth = canvasStyle.width.replace("px", "");
        // Work out the images ratio
        var imageRatio = this.width / this.height;
        // Work out the new height of the canvas, keeping in ratio with the image
        var canvasHeight = canvasWidth / imageRatio;
        // Set the canvas' height in the style tag to be correct
        canvas.style.height = canvasHeight + "px";
        // Set the width/height attributes to be correct (as this is what drawImage uses)
        canvas.width = this.naturalWidth;
        canvas.height = this.naturalHeight;
        // Draw the image at the right width/height
        ctx.drawImage(this, 0, 0);
        setLineScale();
    };
}

function showPreview(event) {
    if (event.target.files.length > 0) {
        var src = URL.createObjectURL(event.target.files[0]);
        openImageOnCanvas(src);
    }
}

function drawBoundryBoxWithName(box, name) {
    var x = box["start"]["x"];
    var y = box["start"]["y"];

    var x2 = box["end"]["x"];
    var y2 = box["end"]["y"];

    var height = y2 - y;
    var width = x2 - x;

    var font_size = Math.round(height * 0.08);
    font_size = Math.max(font_size, 50);

    var text_margin = Math.round(height * 0.02);
    text_margin = Math.max(text_margin, 18);

    ctx.font = "bold " + font_size + "px verdana, sans-serif";
    ctx.strokeRect(x, y, width, height);
    ctx.fillText(name, x, y - text_margin);

}

function setLineScale() {
    img_width = img.naturalWidth;
    img_height = img.naturalHeight;

    linewidth = img_height * 0.0075;

    ctx.strokeStyle = "#00FF00";
    ctx.fillStyle = "#00FF00";
    ctx.lineWidth = Math.round(linewidth);
}
