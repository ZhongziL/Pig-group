$(function () {
	var input = document.getElementById("upload");
	var imageType = /image.*/;
	var getOnloadFunc = function() {
		return function(evt) {
			var img = document.getElementById("iconImage");
			img.src = evt.target.result;
		};
	}
	input.addEventListener("change", function(evt) {
	    for (var i = 0, numFiles = this.files.length; i < numFiles; i++) {
	        var file = this.files[i];
	        if (!file.type.match(imageType)) {
	            continue;
	        }

		    var reader = new FileReader();
		    reader.onload = getOnloadFunc();
		    reader.readAsDataURL(file);
	    }
	}, false);

	$(".close").on('click', function() {
        $("#alert").css("display", "none");
    });

	$('#inputNick').on("click", function () {
		$('#errorNick').css("visibility", "hidden");
	});

	// if submit or not
	$('#saveButton').on("click", function () {
		var iscorrect = true;

		// password
        var password = $("#inputNick").val();
        if (password.length < 1) {
            iscorrect = false;
            $("#errorNick").css("visibility", "visible");
        }

		return iscorrect;
	});
});