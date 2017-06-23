$(function () {
	// passeord
	$('#inputPassword').on("click", function () {
		$('#errorPassword').css("visibility", "hidden");
	});

	// confirm password
	$('#inputConfirmPassword').on("click", function () {
		$('#errorConfirmPassword').css("visibility", "hidden");
	});

	// if submit or not
	$('#saveButton').on("click", function () {
		var iscorrect = true;

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