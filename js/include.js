// function includePreview(category) {

// 	var posts;
// 	var meta = [];

// 	var xhr= new XMLHttpRequest();
// 	xhr.open('GET', 'posts/posts.json', false);
// 	xhr.onreadystatechange= function() {

// 		if (this.readyState !== 4) 
// 			return;
// 		if (this.status !== 200) 
// 			return; // or whatever error handling you want
// 		posts = JSON.parse(this.responseText);
	
// 	};
// 	xhr.send();

// 	for (var i in posts) {
	
// 		var xhr= new XMLHttpRequest();
// 		xhr.open('GET', 'posts/'+posts[i]+'/meta-data.json', true);
// 		xhr.onreadystatechange= function() {
	
// 			if (this.readyState !== 4) 
// 				return;
// 			if (this.status !== 200) 
// 				return; // or whatever error handling you want
// 			meta.push(JSON.parse(this.responseText));

// 			if (i == posts.length-1) {
				
// 				function compareTime(a, b) {
// 					if (a["time"] < b["time"])
// 						return -1;
// 					if (a["time"] > b["time"])
// 						return 1;
// 					return 0;
// 				}
// 				meta.sort(compareTime);

// 				for (var j in meta) {
		
// 					var folder = meta[j]["folder"];
// 					var xhr = new XMLHttpRequest();
// 					xhr.open('GET', 'posts/'+folder+'/preview.html', true);
// 					xhr.onreadystatechange = function() {
				
// 						if (this.readyState !== 4) 
// 							return;
// 						if (this.status !== 200) 
// 							return; // or whatever error handling you want
// 						meta[j]["preview"] = this.responseText;
						
// 						if (j == meta.length-1) {
// 							list = document.getElementById("list");
// 							for (var k in meta)
// 								list.innerHTML += meta[k]["preview"]			
// 						}
// 					};
// 					xhr.send();
	
// 	}

// 			}
		
// 		};
// 		xhr.send();	
	
// 	}

	

// }


function includePreview(category) {

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

	for (var i in posts) {
	
		var xhr= new XMLHttpRequest();
		xhr.open('GET', 'posts/'+posts[i]+'/meta-data.json', false);
		xhr.onreadystatechange = function() {
	
			if (this.readyState !== 4) 
				return;
			if (this.status !== 200) 
				return; // or whatever error handling you want
			meta.push(JSON.parse(this.responseText));

		};
		xhr.send();	
	
	}

	for (var i in meta) {

		var folder = meta[i]["folder"];
		var xhr = new XMLHttpRequest();
		xhr.open('GET', 'posts/'+folder+'/preview.html', false);
		xhr.onreadystatechange = function() {
	
			if (this.readyState !== 4) 
				return;
			if (this.status !== 200) 
				return; // or whatever error handling you want
			meta[i]["preview"] = this.responseText;
			
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


	list = document.getElementById("list");
	for (var i in meta) {
		var valid = category == "latest";
		var tags = meta[i]["tags"];
		if (!valid)
			for (var j in tags)
				if (tags[j] == category)
					valid = true;
		if (valid)
			list.innerHTML += meta[i]["preview"];
	}
}
