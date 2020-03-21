function includePreview(category) {

	list = document.getElementById("list");
	posts = readDirectory("posts");

	// var xhr= new XMLHttpRequest();
	// xhr.open('GET', 'posts/'+post_name+'/preview.html', true);
	// xhr.onreadystatechange= function() {
		// if (this.readyState !== 4) return;
		// if (this.status !== 200) return; // or whatever error handling you want
		// document.getElementById(post_name).innerHTML= this.responseText;
	// };
	// xhr.send();
}

function readDirectory(dir) {

	var filesystem = require("fs");
	var results = [];

	filesystem.readdirSync(dir).forEach(function(file) {

		file = dir+'/'+file;
		var stat = filesystem.statSync(file);

		if (stat && stat.isDirectory()) {
			results = results.concat(_getAllFilesFromFolder(file))
		} else results.push(file);

	});

	return results;
};
