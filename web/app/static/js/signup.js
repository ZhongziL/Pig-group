$(function () {
    var isPhoneChecked = $("#byPhone").attr('checked')
    var PhoneSelect = true;
    if(isPhoneChecked == 'checked') {
        PhoneSelect = true;
    } else {
        PhoneSelect = false;
    }

    var hiddentag = function() {
        $("#errorUsername").css("visibility", "hidden");
        $("#errorPhone").css("visibility", "hidden");
        $("#errorCode").css("visibility", "hidden");
        $("#errorEmail").css("visibility", "hidden");
        $("#errorPassword").css("visibility", "hidden");
        $("#errorPasswordConfirm").css("visibility", "hidden");
    }

    $("#byPhone").on("click", function () {
        PhoneSelect = true;
        $('#byEmail').attr('checked', false);
        $('#phoneMethod').css("display", "block");
        $('#emailMethod').css("display", "none");
        hiddentag()
    });

    $(".close").on('click', function() {
        $("#flash_alert").css("display", "none");
    });

    $("#byEmail").on("click", function () {
        PhoneSelect = false;
        $('#byPhone').attr('checked', false);
        $('#phoneMethod').css("display", "none");
        $('#emailMethod').css("display", "block");
        hiddentag()
    });

    $("#username").on("click", function () {
        $("#errorUsername").css("visibility", "hidden");
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

    $("#password").on("click", function () {
        $("#errorPassword").css("visibility", "hidden");
    });

    $("#password_confirm").on("click", function () {
        $("#errorPasswordConfirm").css("visibility", "hidden");
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
        $("#errorPasswordConfirm").html('再次输入密码');
        var iscorrect = true;

        var username = $('#username').val();
        // username
        if (username === '') {
            iscorrect = false;
            //$("#errorUsername").css("display", "block");
            $("#errorUsername").css("visibility", "visible");
            
        }

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

        // password
        var password = $("#password").val();
        if (password.length < 6) {
            iscorrect = false;
            $("#errorPassword").css("visibility", "visible");
        }

        // confirm password
        var password_confirm = $("#password_confirm").val();
        if (password_confirm.length < 6) {
            iscorrect = false;
            $("#errorPasswordConfirm").css("visibility", "visible");
        }

        if (password !== password_confirm) {
            iscorrect = false;
            $("#errorPasswordConfirm").css("visibility", "visible");
            $("#errorPasswordConfirm").html('密码不一致');
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