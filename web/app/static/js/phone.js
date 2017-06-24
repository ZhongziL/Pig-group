$(function () {
	// phone number
	$('#inputPhone').on("click", function () {
		$('#errorPhone').css("visibility", "hidden");
	});

	// Verification code
	$('#inputVcode').on("click", function () {
		$('#errorCode').css("visibility", "hidden");
	});

	$(".close").on('click', function() {
        $("#alert").css("display", "none");
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

		return iscorrect;
	});
});