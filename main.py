import codecs
import os
from slugify import slugify
import json
#leer templates
f=codecs.open("templates/blog-template.html", encoding="utf8")
blogTemplate = f.read()
f=codecs.open("templates/post-template.html", encoding="utf8")
postTemplate = f.read()
f=codecs.open("templates/thumb-template.html", encoding="utf8")
thumbTemplate = f.read()
#Revisar posts
postsLists = []
for file in os.listdir("posts"):
    if file.endswith(".json"):
        print(os.path.join("posts", file))
        postsLists.append(file)

blog= open("blog.html", "w")


thumbnailcontent = ""
for jsonfile in postsLists:
    tempthumb = thumbTemplate
    temppost = postTemplate
    # lee el archivo json
    datafile =  open("posts/"+ file, "r")
    # parse post:
    datapost = json.load(datafile)
    print(datapost["titulo"]) 
    tempthumb = tempthumb.replace('{{heading}}',datapost["titulo"])
    tempthumb = tempthumb.replace('{{content}}',datapost["contenido"][:350])
    tempthumb = tempthumb.replace('{{image}}',"posts/" + file.replace("json","jpg"))
    tempthumb = tempthumb.replace('{{postURL}}',"blog/" + slugify(datapost["titulo"]) + ".html")
    
    temppost = temppost.replace('{{heading}}',datapost["titulo"])
    temppost = temppost.replace('{{date}}',datapost["fecha"])
    temppost = temppost.replace('{{content}}',datapost["contenido"])
    temppost = temppost.replace('{{image}}',"posts/" + file.replace("json","jpg"))
    temppostHTML= open("blog/" + slugify(datapost["titulo"]) + ".html", "w")
    temppostHTML.write(temppost)
    thumbnailcontent += tempthumb

blog.write(blogTemplate.replace('{{thumbnails}}',thumbnailcontent))


    

