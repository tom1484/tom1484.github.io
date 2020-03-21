import json
import os

post_name = input("post_name: ")

posts = json.loads(open("posts.json", 'r').read())
posts_writer = open("posts.json", 'w')

if post_name in posts:
    posts.remove(post_name)
    posts_writer.write(json.dumps(posts))
    os.system("rm -r "+post_name)
