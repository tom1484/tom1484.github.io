import os
import sys
import json
import time

post_name = input("post_name: ")
if os.path.exists(post_name) == False: 
    os.system("mkdir "+post_name)
else:
    if_override = input("override? (y/n) ")
    while if_override != "y" and if_override != 'n':
        if_override = input("override? (y/n) ")
    if if_override == 'n':
        sys.exit()

preview_path = post_name+"/preview.html"
detail_path = post_name+"/detail.html"
meta_path = post_name+"/meta-data.json"
os.system("cp preview_template.html "+preview_path)
os.system("cp detail_template.html "+detail_path)
os.system("cp meta-data_template.json "+meta_path)

title = input("title: ")
author_img = input("author_img: ")
author_name = input("author_name: ")
author_role = input("author_role: ")

tags = []
tag = input("add tag: ")
while len(tag) > 0:
    tags.append(tag)
    tag = input("add tag: ")

tags_text = ""
for tag in tags:
    tags_text += "<li>\n"
    tags_text += "\t<a href=\"#\">#"
    tags_text += tag
    tags_text += "</a>\n"
    tags_text += "</li>\n"

date_text = time.strftime("%b %d, %Y", time.localtime()) 

preview = open(preview_path, "r").read()
preview_writer = open(preview_path, "w")
detail = open(detail_path, "r").read()
detail_writer = open(detail_path, "w")
meta = json.loads(open(meta_path, "r").read())
meta_writer = open(meta_path, "w")

preview = preview.replace("_title", title)
preview = preview.replace("_author_img", author_img)
preview = preview.replace("_author_name", author_name)
preview = preview.replace("_author_role", author_role)
preview = preview.replace("_tags", tags_text)
preview = preview.replace("_date", date_text)
preview = preview.replace("_folder", post_name)

preview_writer.write(preview)

detail = detail.replace("_title", title)
detail = detail.replace("_author_img", author_img)
detail = detail.replace("_author_name", author_name)
detail = detail.replace("_author_role", author_role)
detail = detail.replace("_tags", tags_text)
detail = detail.replace("_date", date_text)
detail = detail.replace("_folder", post_name)

detail_writer.write(detail)

meta["title"] = title
meta["author_img"] = author_img
meta["author_name"] = author_name
meta["author_role"] = author_role
meta["tags"] = tags
meta["date"] = date_text

meta_writer.write(json.dumps(meta))
