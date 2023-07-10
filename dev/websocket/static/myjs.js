function submitname(elementname, respname){
	let name = document.getElementById(elementname).value;
	$.ajax({
		async: true,
		type: "post",
		url: "name",
		data: {name: name}
	}).done(function(response){
		console.log(response);
		document.getElementById(respname).innerHTML = 'Hello: '+response+' !';
	}).fail(function(error){
		console.log("error received: "+error);
	});
}