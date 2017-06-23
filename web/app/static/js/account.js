$(function () {
	// phone number
	$('#inputPhone').on("click", function () {
		$('#errorPhone').css("visibility", "hidden");
	});

	// Verification code
	$('#inputVcode').on("click", function () {
		$('#errorCode').css("visibility", "hidden");
	});

	// email
	$('#inputEmail').on("click", function () {
		$('#errorEmail').css("visibility", "hidden");
	});

	// if submit or not
	$('#saveButton').on("click", function () {
		var iscorrect = true;

		// check phone number
		var phonePattern = /^1[0-9]{10}/;
        var phone = $('#inputPhone').val();
        if (!(phonePattern.test(phone))) {
            iscorrect = false;
            $("#errorPhone").css("visibility", "visible");
        }

		// check verification code
		var code = $("#inputVcode").val();
        if (code === '') {
            iscorrect = false;
            $("#errorCode").css("visibility", "visible");
        }

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