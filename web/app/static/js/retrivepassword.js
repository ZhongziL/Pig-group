$(function () {
    var isPhoneChecked = $("#byPhone").attr('checked')
    var PhoneSelect = true;
    if(isPhoneChecked == 'checked') {
        PhoneSelect = true;
    } else {
        PhoneSelect = false;
    }

    var hiddentag = function() {
        $("#errorPhone").css("visibility", "hidden");
        $("#errorCode").css("visibility", "hidden");
        $("#errorEmail").css("visibility", "hidden");
    }

    $("#byPhone").on("click", function () {
        PhoneSelect = true;
        $('#byEmail').attr('checked', false);
        $('#phoneMethod').css("display", "block");
        $('#emailMethod').css("display", "none");
        hiddentag()
    });

    $("#byEmail").on("click", function () {
        PhoneSelect = false;
        $('#byPhone').attr('checked', false);
        $('#phoneMethod').css("display", "none");
        $('#emailMethod').css("display", "block");
        hiddentag()
    });

    $("#telnumber").on("click", function () {
        $("#errorPhone").css("visibility", "hidden");
    });

    $("#idcode").on("click", function () {
        $("#errorCode").css("visibility", "hidden");
    });

    $("#email").on("click", function () {
        $("#errorEmail").css("visibility", "hidden");
    });

    $(".close").on('click', function() {
        $("#flash_alert").css("display", "none");
    });

    $("#idcodeBtn").on("click", function() {
        var iscorrect = true;
        var phonePattern = /^1[0-9]{10}/;
        var phone = $('#telnumber').val();
        if (!(phonePattern.test(phone))) {
            iscorrect = false;
            $("#errorPhone").css("visibility", "visible");
        }
        return iscorrect;
    });

    $("#submitBtn").on("click", function () {
        var iscorrect = true;

        // phone
        var phonePattern = /^1[0-9]{10}/;
        var phone = $('#telnumber').val();
        if (PhoneSelect && !(phonePattern.test(phone))) {
            iscorrect = false;
            $("#errorPhone").css("visibility", "visible");
        }

        // code
        var code = $("#idcode").val();
        if (PhoneSelect && code === '') {
            iscorrect = false;
            $("#errorCode").css("visibility", "visible");
        }
        // email
        var emailPattern = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
        var email = $("#email").val();
        if (!PhoneSelect && !(emailPattern.test(email))) {
            iscorrect = false;
            $("#errorEmail").css("visibility", "visible");
        }

        return iscorrect;
    });


});

window.onload = function() {
    //var isPhoneChecked = $("input[name='byPhone']:checked").val();
    var isPhoneChecked = $("#byPhone").attr('checked')
    //alert(isPhoneChecked);
    if (isPhoneChecked == "checked") {
        //$('#byEmail').attr('checked', false);
        $('#phoneMethod').css("display", "block");
        $('#emailMethod').css("display", "none");
    } else {
        //$('#byPhone').attr('checked', false);
        $('#phoneMethod').css("display", "none");
        $('#emailMethod').css("display", "block");
    }
}