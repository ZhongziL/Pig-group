$(function () {
    // original password
	$('#inputOriginalPassword').on("click", function () {
		$('#errorOriginalPassword').css("visibility", "hidden");
	});

	// password
	$('#inputPassword').on("click", function () {
		$('#errorPassword').css("visibility", "hidden");
	});

	// confirm password
	$('#inputConfirmPassword').on("click", function () {
		$('#errorConfirmPassword').css("visibility", "hidden");
	});

	$(".close").on('click', function() {
        $("#alert").css("display", "none");
    });

	// if submit or not
	$('#saveButton').on("click", function () {
		var iscorrect = true;
        // original password
        var Oripassword = $("#inputOriginalPassword").val();
        if (Oripassword.length < 6) {
            iscorrect = false;
            $("#errorOriginalPassword").css("visibility", "visible");
        }
		// password
        var password = $("#inputPassword").val();
        if (password.length < 6) {
            iscorrect = false;
            $("#errorPassword").css("visibility", "visible");
        }

        // confirm password
        var password_confirm = $("#inputConfirmPassword").val();
        if (password_confirm.length < 6 || password_confirm !== password) {
            iscorrect = false;
            $("#errorConfirmPassword").css("visibility", "visible");
        }

		return iscorrect;
	});
});