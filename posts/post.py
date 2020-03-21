import os
import sys
import json
import time

post_name = input("post_name: ")
preview_path = post_name+"/preview.html"
detail_path = post_name+"/detail.html"
meta_path = post_name+"/meta-data.json"

if not os.path.exists(post_name): 
    os.system("mkdir "+post_name)
    os.system("cp templates/preview_template.html "+preview_path)
    os.system("cp templates/detail_template.html "+detail_path)
    os.system("cp templates/meta-data_template.json "+meta_path)
    
    posts = json.loads(open("posts.json", "r").read())
    posts_writer = open("posts.json", "w")
    posts.append(post_name)
    posts_writer.write(json.dumps(posts))

    sys.exit()

meta = json.loads(open(meta_path, 'r').read())

if meta["title"] == "":
    meta["title"] = post_name
if meta["folder"] == "":
    meta["folder"] = post_name
if meta["author_img"] == "":
    meta["author_img"] = "author_mini.png"
if meta["author_name"] == "":
    meta["author_name"] = "Tom Chen"    
if meta["author_role"] == "":
    meta["author_role"] = "Admin"
if meta["date"] == "":
    meta["date"] = time.strftime("%b %d, %Y %I:%M %p", time.localtime()) 
# if "" not in meta:
    # meta[""] = 

title = meta["title"]
author_img = meta["author_img"]
author_name = meta["author_name"]
author_role = meta["author_role"]

tags = ""
for tag in meta["tags"]:
    tags += "<li>\n"
    tags += "\t<a href=\"#\">#"
    tags += tag
    tags += "</a>\n"
    tags += "</li>\n"

date = meta["date"] 

preview = open(preview_path, "r").read()
preview_writer = open(preview_path, "w")
detail = open(detail_path, "r").read()
detail_writer = open(detail_path, "w")
meta_writer = open(meta_path, "w")

preview = preview.replace("_title", title)
preview = preview.replace("_author_img", author_img)
preview = preview.replace("_author_name", author_name)
preview = preview.replace("_author_role", author_role)
preview = preview.replace("_tags", tags)
preview = preview.replace("_date", date)
preview = preview.replace("_folder", post_name)

preview_writer.write(preview)

detail = detail.replace("_title", title)
detail = detail.replace("_author_img", author_img)
detail = detail.replace("_author_name", author_name)
detail = detail.replace("_author_role", author_role)
detail = detail.replace("_tags", tags)
detail = detail.replace("_date", date)
detail = detail.replace("_folder", post_name)

detail_writer.write(detail)

meta_writer.write(json.dumps(meta))
