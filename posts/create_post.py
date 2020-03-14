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
os.system("cp template.html "+post_name+"/preview.html")

title = input("title: ")
author_img = input("author_img: ")
author_name = input("author_name: ")
author_role = input("author_role: ")

tags = []
tag = input("add tag: ")
while len(tag) > 0:
    tags.append(tag)
    tag = input("add tag: ")

preview = open(preview_path, "r").read()
preview_writer = open(preview_path, "w")

preview = preview.replace("_title", title)
preview = preview.replace("_author_img", author_img)
preview = preview.replace("_author_name", author_name)
preview = preview.replace("_author_role", author_role)

tags_text = ""
for tag in tags:
    tags_text += "\t\t\t\t\t\t<li>\n"
    tags_text += "\t\t\t\t\t\t\t<a href=\"#\">#"
    tags_text += tag
    tags_text += "</a>\n"
    tags_text += "\t\t\t\t\t\t</li>\n"
preview = preview.replace("_tags", tags_text)

date_text = time.strftime("%b %d, %Y", time.localtime()) 
preview = preview.replace("_date", date_text)

preview_writer.write(preview)
