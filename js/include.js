function includePreview(post_name) {
	var xhr= new XMLHttpRequest();
	xhr.open('GET', 'posts/'+post_name+'/preview.html', true);
	xhr.onreadystatechange= function() {
		if (this.readyState !== 4) return;
		if (this.status !== 200) return; // or whatever error handling you want
		document.getElementById(post_name).innerHTML= this.responseText;
	};
	xhr.send();
}

function includeDetail(post_name) {
	var xhr= new XMLHttpRequest();
	xhr.open('GET', 'posts/'+post_name+'/detail.html', true);
	xhr.onreadystatechange= function() {
		if (this.readyState !== 4) return;
		if (this.status !== 200) return; // or whatever error handling you want
		document.getElementById(post_name).innerHTML= this.responseText;
	};
	xhr.send();
}
