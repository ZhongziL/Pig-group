$(function () {
    $("#byPhone").on("click", function () {
        $('#byEmail').attr('checked', false);
        $('#phoneMethod').css("display", "block");
        $('#emailMethod').css("display", "none");
    });

    $("#byEmail").on("click", function () {
        $('#byPhone').attr('checked', false);
        $('#phoneMethod').css("display", "none");
        $('#emailMethod').css("display", "block");
    });
});