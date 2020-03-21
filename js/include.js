function includePreview(category) {

	var list = document.getElementById("list");
	var posts;
	var meta = [];

	var xhr= new XMLHttpRequest();
	xhr.open('GET', 'posts/posts.json', false);
	xhr.onreadystatechange= function() {

		if (this.readyState !== 4) 
			return;
		if (this.status !== 200) 
			return; // or whatever error handling you want
		posts = JSON.parse(this.responseText);
	
	};
	xhr.send();

	for (var post in posts) {
	
		var xhr= new XMLHttpRequest();
		xhr.open('GET', 'posts/'+posts[post]+'/meta-data.json', false);
		xhr.onreadystatechange= function() {
	
			if (this.readyState !== 4) 
				return;
			if (this.status !== 200) 
				return; // or whatever error handling you want
			meta.push(JSON.parse(this.responseText));
		
		};
		xhr.send();	
	
	}

	function compareTime(a, b) {
		if (a["time"] < b["time"])
			return -1;
		if (a["time"] > b["time"])
			return 1;
		return 0;
	}
	meta.sort(compareTime);
	alert(meta);
	
}
