$(function () {
	$('#title').on('click', function () {
		$('#title').val('');
		$('#title').removeClass('showerror');
	});

	$('#context').on('click', function () {
		$('#context').val('');
		$('#context').removeClass('showerror');
	});

	// if submit or not
	$("#submitBtn").on("click", function () {
		var iscorrect = true;

		// check if the title is null or not
		var title = $('#title').val();
		if (title.length < 1) {
			$('#title').val('标题不能为空');
			$('#title').addClass('showerror');
			iscorrect = false;
		}

		// check if the context is null or not
		var context = $('#context').val();
		if (context.length < 1) {
			$('#context').val("内容不能为空");
			$('#context').addClass("showerror");
			iscorrect = false;
		}

		return iscorrect;
	});
});