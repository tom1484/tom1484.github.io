function includePreview(category) {

	var list = document.getElementById("list");
	var posts;
	var posts_meta = [];

	var xhr= new XMLHttpRequest();
	xhr.open('GET', 'posts/posts.json', false);
	xhr.onreadystatechange= function() {
		if (this.readyState !== 4) return;
		if (this.status !== 200) return; // or whatever error handling you want
		posts = JSON.parse(this.responseText);
	};
	xhr.send();

	for (var post in posts) {
		
		var xhr= new XMLHttpRequest();
		xhr.open('GET', 'posts/posts.json', true);
		xhr.onreadystatechange= function() {
			if (this.readyState !== 4) return;
			if (this.status !== 200) return; // or whatever error handling you want
			posts_meta.push(JSON.parse(this.responseText));
		};
		xhr.send();
		
	}
	// alert(posts_meta);
	
}
