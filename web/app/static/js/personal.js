$(function () {
	$("#jump").on("click", function () {
		window.open("profile.html");
	});

	$("#answers").on("click", function () {
		$('#answers').css("font-weight", "bold");
		$('#articles').css("font-weight", "normal");
		$('#answerList').css("display", "block");
        $('#articleList').css("display", "none");
	});

	$("#articles").on("click", function () {
		$('#answers').css("font-weight", "normal");
		$('#articles').css("font-weight", "bold");
		$('#answerList').css("display", "none");
        $('#articleList').css("display", "block");
	});

	$("#following").on("click", function () {
		$('#following').css("font-weight", "bold");
		$('#follower').css("font-weight", "normal");
		$('#followingList').css("display", "block");
        $('#followerList').css("display", "none");
	});

	$("#follower").on("click", function () {
		$('#following').css("font-weight", "normal");
		$('#follower').css("font-weight", "bold");
		$('#followingList').css("display", "none");
        $('#followerList').css("display", "block");
	});
});

