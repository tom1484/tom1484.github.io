import os
import sys
import json
import time
import re

post_name = input("post_name: ")
preview_path = post_name+"/preview.html"
detail_path = post_name+"/detail.html"
meta_path = post_name+"/meta-data.json"

# os.system("cp templates/preview_template.html "+preview_path)
# os.system("cp templates/detail_template.html "+detail_path)
# os.system("cp templates/meta-data_template.json "+meta_path)

if not os.path.exists(post_name): 
    # create post
    os.system("mkdir "+post_name)
    os.system("cp templates/preview_template.html "+preview_path)
    os.system("cp templates/detail_template.html "+detail_path)
    os.system("cp templates/meta-data_template.json "+meta_path)
    
    # add post to posts list
    posts = json.loads(open("posts.json", "r").read())
    posts_writer = open("posts.json", "w")
    posts.append(post_name)
    posts_writer.write(json.dumps(posts))

    sys.exit()

# update meta
else: 
    preview = open(preview_path, "r").read()
    detail = open(detail_path, "r").read()
    meta = json.loads(open(meta_path, 'r').read())

    # copy content
    content_pattern = re.compile(r'<!-- content -->.*<!-- content -->', re.DOTALL)
    preview_content = re.search(content_pattern, preview).group(0)
    detail_content = re.search(content_pattern, detail).group(0)
    
    # replace files by new ones
    os.system("cp templates/preview_template.html "+preview_path)
    os.system("cp templates/detail_template.html "+detail_path)

    # insert old content
    preview = open(preview_path, "r").read()
    detail = open(detail_path, "r").read()
    preview = re.sub("<!-- content -->\n<!-- content -->", preview_content, preview)
    detail = re.sub("<!-- content -->\n<!-- content -->", detail_content, detail)

# create file writers
preview_writer = open(preview_path, "w")
detail_writer = open(detail_path, "w")
meta_writer = open(meta_path, "w")

# initialize meta
meta["folder"] = post_name
meta["date"] = time.strftime("%b %d, %Y %I:%M %p", time.localtime()) 
meta["time"] = time.time()

if meta["title"] == "":
    meta["title"] = post_name
if meta["author_img"] == "":
    meta["author_img"] = "author_mini.png"
if meta["author_name"] == "":
    meta["author_name"] = "Tom Chen"    
if meta["author_role"] == "":
    meta["author_role"] = "Admin"
# if "" not in meta:
    # meta[""] = 

title = meta["title"]
author_img = meta["author_img"]
author_name = meta["author_name"]
author_role = meta["author_role"]
date = meta["date"] 

# add tags
tags = ""
for tag in meta["tags"]:
    tags += "<li>\n"
    tags += "\t<a href=\"#\">#"
    tags += tag
    tags += "</a>\n"
    tags += "</li>\n"

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
