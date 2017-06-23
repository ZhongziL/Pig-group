$(function () {
    $("#submitBtn").on("click", function () {
        $("#errorPasswordConfirm").html('再次输入密码');
        var iscorrect = true;

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
