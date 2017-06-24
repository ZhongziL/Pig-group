$(function () {
	// email
	$('#inputEmail').on("click", function () {
		$('#errorEmail').css("visibility", "hidden");
	});

	$(".close").on('click', function() {
        $("#alert").css("display", "none");
    });

	// if submit or not
	$('#saveButton').on("click", function () {
		var iscorrect = true;

		// check email
		var emailPattern = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
        var email = $("#inputEmail").val();
        if (!(emailPattern.test(email))) {
            iscorrect = false;
            $("#errorEmail").css("visibility", "visible");
        }

		return iscorrect;
	});
});