function includePreview(category) {

	list = document.getElementById("list");

	var xhr= new XMLHttpRequest();
	xhr.open('GET', 'posts/posts.json', true);
	xhr.onreadystatechange= function() {
		if (this.readyState !== 4) return;
		if (this.status !== 200) return; // or whatever error handling you want
		alert(this.responseText);
	};
	xhr.send();
}
