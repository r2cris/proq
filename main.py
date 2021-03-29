import codecs
import os
from slugify import slugify
import json
from datetime import datetime
import time
#leer templates
f=codecs.open("templates/blog-template.html", encoding="utf8")
blogTemplate = f.read()
f=codecs.open("templates/home-template.html", encoding="utf8")
homeTemplate = f.read()
f=codecs.open("templates/post-template.html", encoding="utf8")
postTemplate = f.read()
f=codecs.open("templates/thumb-template.html", encoding="utf8")
thumbTemplate = f.read()
f=codecs.open("templates/blog-home-section.html", encoding="utf8")
blogHomeSection = f.read()
#Revisar posts
postsLists = []
destacados = []
for file in os.listdir("posts"):
    if file.endswith(".json"):
        print(os.path.join("posts", file))
        postsLists.append(file)

blog= open("blog.html", "w",encoding="utf-8")
index= open("index.html", "w",encoding="utf-8")

for jsonfile in postsLists:
    # lee el archivo json
    datafile =  open("posts/"+ jsonfile, "r",encoding="utf-8")
    # parse post:
    datapost = json.load(datafile)
    print(datapost["titulo"]) 
    if datapost["destacado"]:
        destacados.append(jsonfile)

def GetDestacado(dateValue):
    for dest in destacados:
        tempdatafile =  open("posts/"+ dest, "r",encoding="utf-8")
        datapostfeatured = json.load(tempdatafile)
        date_time_obj =  datetime.strptime(datapostfeatured["fecha"], "%d/%m/%Y")
        if date_time_obj == dateValue:
            return dest



#Asignar articulos destacados
orderTimePost = []
for dest in destacados:
    datafile =  open("posts/"+ dest, "r",encoding="utf-8")
    datapostfeatured = json.load(datafile)
    date_time_obj =  datetime.strptime(datapostfeatured["fecha"], "%d/%m/%Y")
    orderTimePost.append(date_time_obj)

orderTimePost = sorted(orderTimePost,reverse=True)
featuredPostItems = {
  "header-top-destacado": "",
  "date-top-destacado": "",
  "postURL-destacado-top": "",
  "header-destacado-1": "",
  "date-destacado-1": "",
  "postURL-destacado-1":"",
  "header-destacado-2": "",
  "date-destacado-2": "",
  "postURL-destacado-2":"",
  "header-destacado-3": "",
  "date-destacado-3": "",
  "postURL-destacado-3":""
}
destCounter = 0
tempBlogSectionHome = blogHomeSection
#Crear articulos del blog
thumbnailcontent = ""

for odate in orderTimePost:
    destData = GetDestacado(odate)
    datafile =  open("posts/"+ destData, "r",encoding="utf-8")
    datapostfeatured = json.load(datafile)
    
    if destCounter == 0:
        featuredPostItems["header-top-destacado"] = datapostfeatured["titulo"]
        featuredPostItems["date-top-destacado"] = datapostfeatured["fecha"]
        featuredPostItems["postURL-destacado-top"] = "../blog/" + slugify(datapostfeatured["titulo"]) + ".html"
        tempBlogSectionHome = tempBlogSectionHome.replace('{{header-top-destacado}}',datapostfeatured["titulo"])
        tempBlogSectionHome = tempBlogSectionHome.replace('{{date-top-destacado}}',datapostfeatured["fecha"])
        tempBlogSectionHome = tempBlogSectionHome.replace('{{image-top-destacado}}',"posts/" + destData.replace("json","jpg"))
        tempBlogSectionHome = tempBlogSectionHome.replace('{{postURL-destacado-top}}',"blog/" + slugify(datapostfeatured["titulo"]) + ".html")
    if destCounter == 1:
        featuredPostItems["header-destacado-1"] = datapostfeatured["titulo"]
        featuredPostItems["date-destacado-1"] = datapostfeatured["fecha"]
        featuredPostItems["postURL-destacado-1"] = "../blog/" + slugify(datapostfeatured["titulo"]) + ".html"
        tempBlogSectionHome = tempBlogSectionHome.replace('{{header-destacado-1}}',datapostfeatured["titulo"])
        tempBlogSectionHome = tempBlogSectionHome.replace('{{date-destacado-1}}',datapostfeatured["fecha"])
        tempBlogSectionHome = tempBlogSectionHome.replace('{{postURL-destacado-1}}',"blog/" + slugify(datapostfeatured["titulo"]) + ".html")
    if destCounter == 2:
        featuredPostItems['header-destacado-2'] = datapostfeatured["titulo"]
        featuredPostItems["date-destacado-2"] = datapostfeatured["fecha"]
        featuredPostItems["postURL-destacado-2"] = "../blog/" + slugify(datapostfeatured["titulo"]) + ".html"
        tempBlogSectionHome = tempBlogSectionHome.replace('{{header-destacado-2}}',datapostfeatured["titulo"])
        tempBlogSectionHome = tempBlogSectionHome.replace('{{date-destacado-2}}',datapostfeatured["fecha"])
        tempBlogSectionHome = tempBlogSectionHome.replace('{{postURL-destacado-2}}',"blog/" + slugify(datapostfeatured["titulo"]) + ".html")
    if destCounter == 3:
        featuredPostItems["header-destacado-3"] = datapostfeatured["titulo"]
        featuredPostItems["date-destacado-3"] = datapostfeatured["fecha"]
        featuredPostItems["postURL-destacado-3"] = "../blog/" + slugify(datapostfeatured["titulo"]) + ".html"
        tempBlogSectionHome = tempBlogSectionHome.replace('{{header-destacado-3}}',datapostfeatured["titulo"])
        tempBlogSectionHome = tempBlogSectionHome.replace('{{date-destacado-3}}',datapostfeatured["fecha"])
        tempBlogSectionHome = tempBlogSectionHome.replace('{{postURL-destacado-3}}',"blog/" + slugify(datapostfeatured["titulo"]) + ".html")
    destCounter = destCounter + 1


for jsonfile in postsLists:
    tempthumb = thumbTemplate
    temppost = postTemplate
    # lee el archivo json
    datafile =  open("posts/"+ jsonfile, "r",encoding="utf-8")
    # parse post:
    datapost = json.load(datafile)
        
    
    tempthumb = tempthumb.replace('{{heading}}',datapost["titulo"])
    tempthumb = tempthumb.replace('{{content}}',datapost["contenido"][:350])
    tempthumb = tempthumb.replace('{{image}}',"posts/" + jsonfile.replace("json","jpg"))
    tempthumb = tempthumb.replace('{{postURL}}',"blog/" + slugify(datapost["titulo"]) + ".html")
    
    temppost = temppost.replace('{{heading}}',datapost["titulo"])
    temppost = temppost.replace('{{date}}',datapost["fecha"])
    temppost = temppost.replace('{{content}}',datapost["contenido"])
    temppost = temppost.replace('{{image}}',"posts/" + jsonfile.replace("json","jpg"))

    temppost = temppost.replace('{{header-destacado-1}}',featuredPostItems["header-top-destacado"])
    temppost = temppost.replace('{{date-destacado-1}}',featuredPostItems["date-top-destacado"])
    temppost = temppost.replace('{{postURL-destacado-1}}',featuredPostItems["postURL-destacado-top"])
    temppost = temppost.replace('{{header-destacado-2}}',featuredPostItems["header-destacado-1"])
    temppost = temppost.replace('{{date-destacado-2}}',featuredPostItems["date-destacado-1"])
    temppost = temppost.replace('{{postURL-destacado-2}}',featuredPostItems["postURL-destacado-1"])
    temppost = temppost.replace('{{header-destacado-3}}',featuredPostItems["header-destacado-2"])
    temppost = temppost.replace('{{date-destacado-3}}',featuredPostItems["date-destacado-2"])
    temppost = temppost.replace('{{postURL-destacado-3}}',featuredPostItems["postURL-destacado-2"])
    temppostHTML= open("blog/" + slugify(datapost["titulo"]) + ".html", "w",encoding="utf-8")
    temppostHTML.write(temppost)
    thumbnailcontent += tempthumb





index.write(homeTemplate.replace('{{blog-home}}',tempBlogSectionHome))
blog.write(blogTemplate.replace('{{thumbnails}}',thumbnailcontent))


