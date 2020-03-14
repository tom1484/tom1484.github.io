(function() {
function include(post_name) {
	var xhr= new XMLHttpRequest();
	xhr.open('GET', 'posts/'+post_name+'/preview.html', true);
	xhr.onreadystatechange= function() {
		if (this.readyState !== 4) return;
		if (this.status !== 200) return; // or whatever error handling you want
		document.getElementById('y').innerHTML= this.responseText;
	};
	xhr.send();
}
})();
